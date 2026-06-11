# PCB

KiCad projects for the CocktailBerry boards (and room for other PCB-related
components later). JLCPCB fabrication files (Gerbers, drill, BOM, CPL) are
generated headlessly — on release by CI, or locally — with
[KiKit](https://github.com/yaqwsx/KiKit) via
[`scripts/build_fab.py`](../scripts/build_fab.py).

## Layout & conventions

```shell
pcb/<board>/
  <board>.kicad_pcb   # exactly one PCB per board folder
  <board>.kicad_sch   # root schematic (shares the project base name)
  *.kicad_sch         # hierarchical sub-sheets (e.g. a reused pump circuit)
  ...                 # symbols/footprints/etc. live alongside as usual
```

- Each board folder must contain **exactly one** `*.kicad_pcb` (one layout per
  project, no matter how many schematic sheets exist).
- **Hierarchical schematics are fine.** Only the **root** sheet (named after the
  project, like the `.kicad_pcb`) is passed to KiKit; it walks the hierarchy and
  pulls in all sub-sheets — so a pump circuit reused 10× flattens into the
  BOM/CPL automatically.
- Components to be assembled need their **LCSC part number** in the `MPN`
  schematic field (see `LCSC_FIELD` in `scripts/build_fab.py`). Parts without it
  appear in the BOM without an LCSC code and won't be placed.

## Running

KiKit + KiCad (`pcbnew`) are **not** uv dependencies; install them separately
(`apt-get install kicad` + `pip install kikit` on CI). Then:

```bash
uv run python scripts/build_fab.py            # all boards -> dist/<board>.zip
uv run python scripts/build_fab.py cbb-gpio    # a single board
```
