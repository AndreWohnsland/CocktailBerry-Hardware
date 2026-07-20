# CAD sources

FreeCAD sources for the machines. Manufacturing artifacts (STEP + STL) are
generated headlessly - on release by CI, or locally - via
[`scripts/export_freecad.py`](../scripts/export_freecad.py) (runs under FreeCAD's
`freecadcmd`) and [`scripts/build_artifacts.py`](../scripts/build_artifacts.py)
(the uv-driven orchestrator that zips per machine).

## Layout & conventions

```shell
cad/machines/<machine>/
  *.FCStd        # exported  (files in the folder ROOT)
  lib/           # helpers / imported sources - NOT exported (any subfolder)
  export.toml    # optional: pin which objects to export per file
cad/accessories/ # shared extra hardware - same conventions, own export unit
```

- **File selection:** every `*.FCStd` in a machine-folder **root** is exported.
  Put helper or imported documents in a **subfolder** (e.g. `lib/`) to skip them.
- **Object selection** per file:
  - One result body in the file → exported automatically, no config needed.
  - Multiple candidates (e.g. a base that forks into variants) → the run fails
    and lists them, so you pin the ones you want in `export.toml`, keyed by the
    file name without `.FCStd`:
    ```toml
    [main_body]
    objects = ["MainBodyStandard", "MainBodyTall", "MainBodyCompact"]
    ```
  - Output files are named after each object's **Label** - name objects
    meaningfully.

## Running

FreeCAD is **not** a uv dependency; install it separately (`apt-get install
freecad` on CI). Then:

```bash
uv run python scripts/build_artifacts.py                # all units -> dist/<unit>.zip
uv run python scripts/build_artifacts.py mk3 accessories # selected units
```
