"""Render KiCad DRC JSON reports as a markdown summary (run with uv).

    uv run python scripts/drc_report.py cbb-gpio cbb-slim

Reads dist/drc-<board>.json (as written by ``kicad-cli pcb drc --format json``)
and prints markdown to stdout. The PR checks workflow posts this as the
"PCBA Review Bot" comment. Informational only -- it never fails on violations;
the boards carry known, accepted violations, so pass/fail lives with the
developer's local review, not here.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT / "dist"

# Boards routinely carry dozens of accepted warnings; show them collapsed and
# capped so the comment stays readable. Errors are always shown in full.
MAX_WARNINGS = 20

SEVERITY_ORDER = {"error": 0, "warning": 1}


def table(violations: list[dict]) -> str:
    lines = ["| Check | Description | Where |", "|---|---|---|"]
    for v in violations:
        where = "; ".join(i["description"] for i in v.get("items", [])[:2])
        lines.append(f"| `{v['type']}` | {v['description']} | {where} |")
    return "\n".join(lines)


def board_section(board: str) -> str:
    report = json.loads((DIST_DIR / f"drc-{board}.json").read_text())
    findings = report.get("violations", []) + report.get("unconnected_items", [])
    findings.sort(key=lambda v: SEVERITY_ORDER.get(v["severity"], 2))
    errors = [v for v in findings if v["severity"] == "error"]
    warnings = [v for v in findings if v["severity"] != "error"]

    if not findings:
        return f"### `{board}` — ✅ no findings\n"

    out = [f"### `{board}` — ❌ {len(errors)} errors, ⚠️ {len(warnings)} warnings\n"]
    if errors:
        out.append(table(errors))
        out.append("")
    if warnings:
        shown = warnings[:MAX_WARNINGS]
        more = f"\n… and {len(warnings) - len(shown)} more." if len(warnings) > len(shown) else ""
        out.append(f"<details><summary>⚠️ {len(warnings)} warnings</summary>\n")
        out.append(table(shown) + more)
        out.append("\n</details>\n")
    return "\n".join(out)


def main(boards: list[str]) -> None:
    if not boards:
        sys.exit("usage: drc_report.py <board> [board ...]")
    print("## 🤖 PCBA Review Bot\n")
    print("DRC results for the boards changed in this PR. Informational only — known, accepted violations are expected and do not block the merge.\n")
    for board in boards:
        print(board_section(board))


if __name__ == "__main__":
    main(sys.argv[1:])
