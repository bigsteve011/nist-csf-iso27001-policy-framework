#!/usr/bin/env python3
"""Validate the NIST CSF 2.0 <-> ISO/IEC 27001:2022 mapping and regenerate derived docs.

The mapping CSV is the single source of truth. This script:
  1. validates every row (ID formats, known functions, referenced documents exist);
  2. rewrites the "Framework Mapping" section of each policy and procedure
     between the <!-- mapping:start --> and <!-- mapping:end --> markers;
  3. regenerates mapping/COVERAGE.md (coverage by function, Annex A coverage, gaps).

Usage:
  python scripts/build_mapping.py           # validate and regenerate
  python scripts/build_mapping.py --check   # validate only; fail if generated files are stale (CI)
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAPPING = ROOT / "mapping" / "csf-iso27001-mapping.csv"
COVERAGE = ROOT / "mapping" / "COVERAGE.md"
DOC_DIRS = {"POL": ROOT / "policies", "PRC": ROOT / "procedures"}

FUNCTIONS = ["GOVERN", "IDENTIFY", "PROTECT", "DETECT", "RESPOND", "RECOVER"]
FUNCTION_PREFIX = {"GOVERN": "GV", "IDENTIFY": "ID", "PROTECT": "PR",
                   "DETECT": "DE", "RESPOND": "RS", "RECOVER": "RC"}

CSF_ID = re.compile(r"^(GV|ID|PR|DE|RS|RC)\.[A-Z]{2}-\d{2}$")
ISO_CLAUSE = re.compile(r"^(4|5|6|7|8|9|10)(\.\d+){1,2}$")
ANNEX_A = re.compile(r"^(5\.([1-9]|[1-2]\d|3[0-7])|6\.[1-8]|7\.([1-9]|1[0-4])|8\.([1-9]|[1-2]\d|3[0-4]))$")
DOC_ID = re.compile(r"^(POL|PRC)-\d{2}$")

# ISO/IEC 27001:2022 Annex A themes, used for the coverage summary.
ANNEX_A_THEMES = {"5": ("Organisational", 37), "6": ("People", 8),
                  "7": ("Physical", 14), "8": ("Technological", 34)}

START, END = "<!-- mapping:start -->", "<!-- mapping:end -->"


def split(value: str) -> list[str]:
    return [v.strip() for v in value.split(";") if v.strip()]


def annex_sort_key(control: str) -> tuple[int, int]:
    theme, num = control.split(".")
    return int(theme), int(num)


def load_rows() -> list[dict]:
    with MAPPING.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def find_documents() -> dict[str, Path]:
    docs = {}
    for prefix, folder in DOC_DIRS.items():
        for path in folder.glob(f"{prefix}-*.md"):
            docs[path.name[:6]] = path
    return docs


def validate(rows: list[dict], docs: dict[str, Path]) -> list[str]:
    errors, seen = [], set()
    for n, row in enumerate(rows, start=2):
        where = f"{MAPPING.name}:{n}"
        cid, func = row["csf_id"], row["csf_function"]
        if not CSF_ID.match(cid):
            errors.append(f"{where}: malformed CSF ID '{cid}'")
        if cid in seen:
            errors.append(f"{where}: duplicate CSF ID '{cid}'")
        seen.add(cid)
        if func not in FUNCTIONS:
            errors.append(f"{where}: unknown function '{func}'")
        elif not cid.startswith(FUNCTION_PREFIX[func]):
            errors.append(f"{where}: '{cid}' does not belong to function {func}")
        for clause in split(row["iso_clauses"]):
            if not ISO_CLAUSE.match(clause):
                errors.append(f"{where}: malformed ISO clause '{clause}'")
        for control in split(row["iso_annex_a"]):
            if not ANNEX_A.match(control):
                errors.append(f"{where}: '{control}' is not an ISO 27001:2022 Annex A control")
        if not split(row["iso_clauses"]) and not split(row["iso_annex_a"]):
            errors.append(f"{where}: '{cid}' has no ISO 27001 mapping")
        if row["relationship"] not in {"Strong", "Partial"}:
            errors.append(f"{where}: relationship must be Strong or Partial")
        for field in ("policy", "procedure"):
            for doc in split(row[field]):
                if not DOC_ID.match(doc):
                    errors.append(f"{where}: malformed document ID '{doc}'")
                elif doc not in docs:
                    errors.append(f"{where}: {field} '{doc}' has no matching file")
        if not split(row["policy"]):
            errors.append(f"{where}: '{cid}' is not covered by any policy")
    return errors


def doc_mapping_section(doc_id: str, rows: list[dict]) -> str:
    field = "policy" if doc_id.startswith("POL") else "procedure"
    mine = [r for r in rows if doc_id in split(r[field])]
    lines = [START,
             "_Generated from [`mapping/csf-iso27001-mapping.csv`](../mapping/csf-iso27001-mapping.csv)"
             " by `scripts/build_mapping.py`. Do not edit by hand._", "",
             "| NIST CSF 2.0 | Outcome | ISO 27001 Clauses | ISO 27001 Annex A | Fit |",
             "| :--- | :--- | :--- | :--- | :--- |"]
    for r in mine:
        lines.append(f"| {r['csf_id']} | {r['csf_outcome']} | "
                     f"{', '.join(split(r['iso_clauses'])) or '—'} | "
                     f"{', '.join(split(r['iso_annex_a'])) or '—'} | {r['relationship']} |")
    if not mine:
        lines.append("| — | Supporting document; not directly mapped | — | — | — |")
    lines.append(END)
    return "\n".join(lines)


def render_docs(rows: list[dict], docs: dict[str, Path]) -> dict[Path, str]:
    out = {}
    for doc_id, path in sorted(docs.items()):
        text = path.read_text(encoding="utf-8")
        pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
        if not pattern.search(text):
            raise SystemExit(f"{path.relative_to(ROOT)}: missing mapping markers")
        out[path] = pattern.sub(lambda _: doc_mapping_section(doc_id, rows), text)
    return out


def doc_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def render_coverage(rows: list[dict], docs: dict[str, Path]) -> str:
    by_func = defaultdict(list)
    for r in rows:
        by_func[r["csf_function"]].append(r)

    annex = defaultdict(set)
    for r in rows:
        for c in split(r["iso_annex_a"]):
            annex[c].add(r["csf_id"])
    clauses = sorted({c for r in rows for c in split(r["iso_clauses"])},
                     key=lambda c: [int(p) for p in c.split(".")])

    out = ["# Mapping Coverage Report", "",
           "_Generated by `scripts/build_mapping.py` from `csf-iso27001-mapping.csv`. Do not edit by hand._", "",
           "## Coverage by NIST CSF 2.0 Function", "",
           "| Function | Subcategories Mapped | Strong | Partial | Policies |",
           "| :--- | ---: | ---: | ---: | :--- |"]
    for f in FUNCTIONS:
        rs = by_func[f]
        strong = sum(r["relationship"] == "Strong" for r in rs)
        pols = sorted({p for r in rs for p in split(r["policy"])})
        out.append(f"| {f} | {len(rs)} | {strong} | {len(rs) - strong} | {', '.join(pols)} |")
    strong = sum(r["relationship"] == "Strong" for r in rows)
    out.append(f"| **Total** | **{len(rows)}** | **{strong}** | **{len(rows) - strong}** | |")

    out += ["", "## ISO/IEC 27001:2022 Annex A Coverage", "",
            "| Theme | Controls Referenced | Controls in Theme | Coverage |",
            "| :--- | ---: | ---: | ---: |"]
    for theme, (name, total) in ANNEX_A_THEMES.items():
        n = sum(1 for c in annex if c.split(".")[0] == theme)
        out.append(f"| {theme}. {name} | {n} | {total} | {n / total:.0%} |")
    out += ["", f"ISMS clauses referenced: {', '.join(clauses)}", "",
            "<details><summary>Annex A control → CSF subcategories</summary>", "",
            "| Annex A | CSF Subcategories |", "| :--- | :--- |"]
    for c in sorted(annex, key=annex_sort_key):
        out.append(f"| {c} | {', '.join(sorted(annex[c]))} |")
    out += ["", "</details>", "", "## Document Index", "",
            "| ID | Document | CSF Subcategories |", "| :--- | :--- | ---: |"]
    for doc_id, path in sorted(docs.items()):
        field = "policy" if doc_id.startswith("POL") else "procedure"
        n = sum(doc_id in split(r[field]) for r in rows)
        rel = "../" + path.relative_to(ROOT).as_posix()
        out.append(f"| {doc_id} | [{doc_title(path)}]({rel}) | {n} |")

    partial = [r for r in rows if r["relationship"] == "Partial"]
    out += ["", "## Partial Mappings (review candidates)", "",
            "These subcategories are only partly met by the mapped ISO 27001 requirements "
            "and need supplementary controls or evidence.", "",
            "| CSF | Outcome | Mapped To |", "| :--- | :--- | :--- |"]
    for r in partial:
        iso = ", ".join(split(r["iso_clauses"]) + [f"A.{c}" for c in split(r["iso_annex_a"])])
        out.append(f"| {r['csf_id']} | {r['csf_outcome']} | {iso} |")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if generated files are out of date")
    args = parser.parse_args()

    rows, docs = load_rows(), find_documents()
    errors = validate(rows, docs)
    unused = sorted(d for d in docs if not any(d in split(r["policy"]) + split(r["procedure"]) for r in rows))
    if errors:
        print("Mapping validation failed:", *errors, sep="\n  ")
        return 1

    targets = render_docs(rows, docs)
    targets[COVERAGE] = render_coverage(rows, docs)

    stale = [p for p, text in targets.items()
             if not p.exists() or p.read_text(encoding="utf-8") != text]
    if args.check:
        if stale:
            print("Generated files are out of date. Run: python scripts/build_mapping.py",
                  *[f"  {p.relative_to(ROOT)}" for p in stale], sep="\n")
            return 1
    else:
        for path in stale:
            path.write_text(targets[path], encoding="utf-8")
            print(f"updated {path.relative_to(ROOT)}")

    print(f"OK: {len(rows)} CSF subcategories, {len(docs)} documents.")
    if unused:
        print(f"Note: documents not referenced by the mapping: {', '.join(unused)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
