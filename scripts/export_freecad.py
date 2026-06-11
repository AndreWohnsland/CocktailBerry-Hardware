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


def export_object(obj: DocObject, out_dir: str) -> None:
    base = os.path.join(out_dir, sanitize(obj.Label))
    Part.export([obj], base + ".step")
    mesh = MeshPart.meshFromShape(
        Shape=obj.Shape,
        LinearDeflection=LINEAR_DEFLECTION,
        AngularDeflection=ANGULAR_DEFLECTION,
        Relative=False,
    )
    mesh.write(base + ".stl")
    print(f"  exported {obj.Label} -> {os.path.basename(base)}.{{step,stl}}")


def load_manifest(machine_dir: str) -> dict[str, Any]:
    path = os.path.join(machine_dir, "export.toml")
    if not os.path.exists(path):
        return {}
    with open(path, "rb") as fh:
        return tomllib.load(fh)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: freecadcmd export_freecad.py <machine_dir> <out_dir>")
    machine_dir, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    manifest = load_manifest(machine_dir)

    files = sorted(
        f
        for f in os.listdir(machine_dir)
        if f.lower().endswith(".fcstd") and os.path.isfile(os.path.join(machine_dir, f))
    )
    if not files:
        print(f"no .FCStd files in {machine_dir}")
        return

    errors = []
    for fname in files:
        stem = os.path.splitext(fname)[0]
        print(f"{fname}:")
        doc = FreeCAD.openDocument(os.path.join(machine_dir, fname))
        try:
            wanted = manifest.get(stem, {}).get("objects")
            if wanted:
                by_label = {o.Label: o for o in doc.Objects}
                missing = [w for w in wanted if w not in by_label]
                if missing:
                    errors.append(f"{fname}: objects not found by Label: {missing}")
                    continue
                targets = [by_label[w] for w in wanted]
            else:
                cands = candidates(doc)
                if len(cands) != 1:
                    names = [o.Label for o in cands]
                    errors.append(
                        f"{fname}: {len(cands)} export candidates {names} -- "
                        f"add a [{stem}] entry to export.toml to pick objects"
                    )
                    continue
                targets = cands
            for obj in targets:
                export_object(obj, out_dir)
        finally:
            FreeCAD.closeDocument(doc.Name)

    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)


main()
