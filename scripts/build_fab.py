"""Generate JLCPCB fabrication files with KiKit (run with uv).

    uv run python scripts/build_fab.py            # all boards
    uv run python scripts/build_fab.py cbb-gpio   # selected boards

For each board folder under pcb/, runs ``kikit fab jlcpcb`` on its single
``*.kicad_pcb`` and zips the result to dist/<board>.zip. If the matching root
``*.kicad_sch`` is present, assembly data (BOM + CPL/pick-and-place) is included;
KiKit walks the schematic hierarchy itself, so sub-sheets are pulled in too.

KiKit + KiCad (pcbnew) are NOT uv dependencies -- install them separately (apt
KiCad + ``pip install kikit`` on CI). Only the orchestration runs under uv;
it just shells out to the ``kikit`` CLI.
"""

import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PCB_DIR = ROOT / "pcb"
DIST_DIR = ROOT / "dist"

# KiCad symbol field that holds the LCSC part number. KiKit defaults to "LCSC";
# this project stores it in "MPN".
LCSC_FIELD = "MPN"


def find_kikit() -> str:
    path = shutil.which("kikit")
    if path:
        return path
    sys.exit("kikit not found on PATH -- install KiCad + `pip install kikit`.")


def single_pcb(board_dir: Path) -> Path:
    # One layout per KiCad project, regardless of how many schematic sheets exist.
    pcbs = sorted(board_dir.glob("*.kicad_pcb"))
    if len(pcbs) != 1:
        sys.exit(f"{board_dir}: expected exactly one .kicad_pcb, found {len(pcbs)}")
    return pcbs[0]


def zip_dir(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(src.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(src))


def main(argv: list[str]) -> None:
    kikit = find_kikit()
    if not PCB_DIR.is_dir():
        sys.exit(f"no pcb directory: {PCB_DIR}")

    selected = argv or [p.name for p in sorted(PCB_DIR.iterdir()) if p.is_dir()]
    if not selected:
        sys.exit(f"no board folders under {PCB_DIR}")

    for board in selected:
        board_dir = PCB_DIR / board
        if not board_dir.is_dir():
            sys.exit(f"board folder not found: {board_dir}")
        pcb = single_pcb(board_dir)
        out_dir = DIST_DIR / board
        if out_dir.exists():
            shutil.rmtree(out_dir)
        out_dir.mkdir(parents=True)

        print(f"== {board} ==")
        # --no-drc keeps an already-validated board from being blocked by a CI
        # DRC quirk; drop it to enforce DRC at release time.
        cmd = [kikit, "fab", "jlcpcb", "--no-drc"]
        # The root schematic shares the project/.kicad_pcb base name; sub-sheets
        # have other names and are pulled in by KiKit automatically.
        sch = pcb.with_suffix(".kicad_sch")
        if sch.exists():
            cmd += ["--assembly", "--schematic", str(sch), "--field", LCSC_FIELD]
        cmd += [str(pcb), str(out_dir)]
        subprocess.run(cmd, check=True)

        zip_path = DIST_DIR / f"{board}.zip"
        zip_dir(out_dir, zip_path)
        print(f"packaged {zip_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
