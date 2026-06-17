"""Export STEP + STL from FreeCAD documents for one machine.

Run with FreeCAD's bundled interpreter (NOT uv — uv cannot ``import FreeCAD``):

    freecadcmd scripts/export_freecad.py <machine_dir> <out_dir>

Conventions (see cad/README.md):
  * Every ``*.FCStd`` in the ROOT of <machine_dir> is exported. Helper / imported
    sources live in subfolders and are ignored.
  * Object selection per file:
      - File has an entry in <machine_dir>/export.toml -> exactly those objects
        (matched by Label) are exported.
      - Otherwise the single "result" body is auto-detected. If a file has more
        than one candidate (e.g. a base that forks into variants), the run fails
        and lists the candidates so you can add an export.toml entry.
  * Output naming:
      - Auto-detected single body -> named after the FILE (e.g. DrainingRack.step).
        Bodies are conventionally labelled "Body", so naming by Label would make
        every single-body file collide in the shared out_dir.
      - export.toml-mapped objects -> named after each object's Label.
"""

import os
import sys
import tomllib  # FreeCAD ships Python >= 3.11
from typing import Any

import FreeCAD
import MeshPart
import Part

# FreeCAD ships no type stubs; these aliases keep the signatures readable.
Document = Any
DocObject = Any

LINEAR_DEFLECTION = 0.1  # STL resolution in mm; smaller = finer mesh / bigger files
ANGULAR_DEFLECTION = 0.5


def log(msg: str = "") -> None:
    # Our progress goes to stderr; FreeCAD's verbose console chatter stays on
    # stdout. That lets build_artifacts.py capture the two separately and hide
    # the chatter on a successful run (see its subprocess handling).
    print(msg, file=sys.stderr, flush=True)


def sanitize(name: str) -> str:
    keep = "-_.() "
    return "".join(c if c.isalnum() or c in keep else "_" for c in name).strip()


def candidates(doc: Document) -> list[DocObject]:
    """Terminal solids: objects with a real solid Shape that nothing depends on."""
    out: list[DocObject] = []
    for obj in doc.Objects:
        shape = getattr(obj, "Shape", None)
        if shape is None or shape.isNull() or not shape.Solids:
            continue
        if obj.InList:  # consumed by another feature -> not a final result
            continue
        out.append(obj)
    return out


def export_object(obj: DocObject, out_dir: str, name: str) -> None:
    base = os.path.join(out_dir, sanitize(name))
    Part.export([obj], base + ".step")
    mesh = MeshPart.meshFromShape(
        Shape=obj.Shape,
        LinearDeflection=LINEAR_DEFLECTION,
        AngularDeflection=ANGULAR_DEFLECTION,
        Relative=False,
    )
    mesh.write(base + ".stl")
    stem = os.path.basename(base)
    step_kb = os.path.getsize(base + ".step") / 1024
    stl_kb = os.path.getsize(base + ".stl") / 1024
    # Sizes are a cheap sanity signal: a near-empty file means a broken export.
    log(f"      wrote {stem}.step ({step_kb:,.0f} KB) + {stem}.stl ({stl_kb:,.0f} KB)")


def load_manifest(machine_dir: str) -> dict[str, Any]:
    path = os.path.join(machine_dir, "export.toml")
    if not os.path.exists(path):
        return {}
    with open(path, "rb") as fh:
        return tomllib.load(fh)


def main() -> None:
    # freecadcmd runs as `freecadcmd <script> <args...>`, so sys.argv[0] is the
    # freecadcmd binary and sys.argv[1] is THIS script -- unlike plain Python.
    # Our two real arguments are therefore always the last two entries.
    if len(sys.argv) < 3:
        sys.exit("usage: freecadcmd export_freecad.py <machine_dir> <out_dir>")
    machine_dir, out_dir = sys.argv[-2], sys.argv[-1]
    os.makedirs(out_dir, exist_ok=True)
    manifest = load_manifest(machine_dir)

    files = sorted(
        f
        for f in os.listdir(machine_dir)
        if f.lower().endswith(".fcstd") and os.path.isfile(os.path.join(machine_dir, f))
    )
    if not files:
        log(f"no .FCStd files in {machine_dir}")
        return

    errors = []
    for fname in files:
        stem = os.path.splitext(fname)[0]
        log(f"\n{fname}")
        doc = FreeCAD.openDocument(os.path.join(machine_dir, fname))
        try:
            wanted = manifest.get(stem, {}).get("objects")
            if wanted:
                # Explicitly mapped objects: a file forks into several named
                # variants, so each export is named by its object Label to keep
                # them distinct (e.g. DripTrayNoScale, DripTrayWithScale).
                by_label = {o.Label: o for o in doc.Objects}
                missing = [w for w in wanted if w not in by_label]
                if missing:
                    errors.append(f"{fname}: objects not found by Label: {missing}")
                    continue
                targets = [(by_label[w], w) for w in wanted]
            else:
                # Single result body: name the export after the FILE, not the
                # body Label. Bodies are conventionally labelled "Body", so
                # naming by Label would collide across files in the same machine
                # (all writing Body.step/Body.stl into the shared out_dir).
                cands = candidates(doc)
                if len(cands) != 1:
                    names = [o.Label for o in cands]
                    errors.append(
                        f"{fname}: {len(cands)} export candidates {names} -- "
                        f"add a [{stem}] entry to export.toml to pick objects"
                    )
                    continue
                targets = [(cands[0], stem)]
            for obj, name in targets:
                # Header per part BEFORE the work, so if an export crashes the
                # last line printed names the part that broke. Show the source
                # object only when it differs from the export name (mapped case).
                src = "" if obj.Label == name else f" (object: {obj.Label})"
                log(f"  -> exporting {name}{src}")
                export_object(obj, out_dir, name)
        finally:
            FreeCAD.closeDocument(doc.Name)

    if errors:
        log("\nERRORS:")
        for e in errors:
            log(f"  - {e}")
        sys.exit(1)


main()
