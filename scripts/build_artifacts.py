"""Orchestrate CAD artifact export and packaging (run with uv).

    uv run python scripts/build_artifacts.py                 # all units
    uv run python scripts/build_artifacts.py mk3 accessories # selected units

Export units are the machine folders under cad/machines/ plus cad/accessories/
(shared extra hardware, one unit of its own). For each, this calls FreeCAD's
headless ``freecadcmd`` (see scripts/export_freecad.py) to export STEP + STL,
then zips the results to dist/<unit>.zip.

FreeCAD is NOT a uv dependency -- ``freecadcmd`` (FreeCAD >= 1.1, matching the
version the .FCStd files are authored in) must be on PATH separately. CI unpacks
the official 1.1 AppImage; locally use your FreeCAD install. Only the
orchestration runs under uv.
"""

import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MACHINES_DIR = ROOT / "cad" / "machines"
ACCESSORIES_DIR = ROOT / "cad" / "accessories"
DIST_DIR = ROOT / "dist"
EXPORT_SCRIPT = ROOT / "scripts" / "export_freecad.py"

# Prebuilt files shipped as-is: copied from a unit folder's ROOT into its dist
# output after the FreeCAD export, so they land in the release zip alongside
# the generated STEP/STL (e.g. hand-tuned print profiles with no CAD source).
PREBUILT_PATTERNS = ["*.3mf"]


def find_freecadcmd() -> str:
    for name in ("freecadcmd", "FreeCADCmd"):
        path = shutil.which(name)
        if path:
            return path
    sys.exit("freecadcmd not found on PATH -- install FreeCAD (apt-get install freecad).")


def zip_dir(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(src.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(src))


def main(argv: list[str]) -> None:
    freecadcmd = find_freecadcmd()
    if not MACHINES_DIR.is_dir():
        sys.exit(f"no machines directory: {MACHINES_DIR}")

    # Export units: one per machine, plus cad/accessories (shared extra
    # hardware that belongs to no single machine) as a unit of its own.
    units = {p.name: p for p in sorted(MACHINES_DIR.iterdir()) if p.is_dir()}
    if ACCESSORIES_DIR.is_dir():
        units[ACCESSORIES_DIR.name] = ACCESSORIES_DIR
    if not units:
        sys.exit(f"no machine folders under {MACHINES_DIR}")

    for name in argv or list(units):
        unit_dir = units.get(name)
        if unit_dir is None:
            sys.exit(f"unknown export unit: {name} (expected one of: {', '.join(units)})")
        out_dir = DIST_DIR / name
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True)

        proc = subprocess.run(
            [freecadcmd, str(EXPORT_SCRIPT), str(unit_dir), str(out_dir)],
            capture_output=True,
            text=True,
        )
        # Fold each unit into a collapsible GH Actions group. export_freecad.py
        # writes our progress to stderr (always shown); FreeCAD's verbose console
        # chatter lands on stdout and is only worth surfacing when the run failed,
        # so a green build stays readable.
        print(f"::group::{f'  UNIT: {name}  ':=^60}", flush=True)
        if proc.stderr:
            print(proc.stderr, end="", flush=True)
        if proc.returncode != 0 and proc.stdout:
            print("\n--- freecadcmd console output ---", flush=True)
            print(proc.stdout, end="", flush=True)
        print("::endgroup::", flush=True)
        if proc.returncode != 0:
            sys.exit(f"freecadcmd failed for {name} (exit code {proc.returncode})")

        for pattern in PREBUILT_PATTERNS:
            for f in sorted(unit_dir.glob(pattern)):
                shutil.copy2(f, out_dir / f.name)
                print(f"  copied prebuilt {f.name}", flush=True)

        if not any(f.is_file() for f in out_dir.rglob("*")):
            # Nothing exported (e.g. accessories/ holds no .FCStd yet) -- don't
            # attach an empty zip to the release.
            print(f"  nothing exported for {name} -- skipping zip", flush=True)
            continue
        zip_path = DIST_DIR / f"{name}.zip"
        zip_dir(out_dir, zip_path)
        print(f"  packaged -> {zip_path.relative_to(ROOT)}", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
