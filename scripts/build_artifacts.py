"""Orchestrate CAD artifact export and packaging (run with uv).

    uv run python scripts/build_artifacts.py            # all machines
    uv run python scripts/build_artifacts.py mk3 mk4    # selected machines

For each machine folder under cad/machines/, this calls FreeCAD's headless
``freecadcmd`` (see scripts/export_freecad.py) to export STEP + STL, then zips
the results to dist/<machine>.zip.

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
DIST_DIR = ROOT / "dist"
EXPORT_SCRIPT = ROOT / "scripts" / "export_freecad.py"


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

    selected = argv or [p.name for p in sorted(MACHINES_DIR.iterdir()) if p.is_dir()]
    if not selected:
        sys.exit(f"no machine folders under {MACHINES_DIR}")

    for machine in selected:
        machine_dir = MACHINES_DIR / machine
        if not machine_dir.is_dir():
            sys.exit(f"machine folder not found: {machine_dir}")
        out_dir = DIST_DIR / machine
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True)

        proc = subprocess.run(
            [freecadcmd, str(EXPORT_SCRIPT), str(machine_dir), str(out_dir)],
            capture_output=True,
            text=True,
        )
        # Fold each machine into a collapsible GH Actions group. export_freecad.py
        # writes our progress to stderr (always shown); FreeCAD's verbose console
        # chatter lands on stdout and is only worth surfacing when the run failed,
        # so a green build stays readable.
        print(f"::group::{f'  MACHINE: {machine}  ':=^60}", flush=True)
        if proc.stderr:
            print(proc.stderr, end="", flush=True)
        if proc.returncode != 0 and proc.stdout:
            print("\n--- freecadcmd console output ---", flush=True)
            print(proc.stdout, end="", flush=True)
        print("::endgroup::", flush=True)
        if proc.returncode != 0:
            sys.exit(f"freecadcmd failed for {machine} (exit code {proc.returncode})")

        zip_path = DIST_DIR / f"{machine}.zip"
        zip_dir(out_dir, zip_path)
        print(f"  packaged -> {zip_path.relative_to(ROOT)}", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
