#!/usr/bin/env python3
"""
validate_skills.py — Validate Architecture Agent Skills for correctness.

Usage:
    python scripts/validate_skills.py                          # Validate all skills
    python scripts/validate_skills.py --skill runtime-error-diagnosis  # Validate one skill
    python scripts/validate_skills.py --json                   # Output as JSON
    python scripts/validate_skills.py --strict                 # Fail on warnings

Checks:
  - SKILL.md exists
  - YAML frontmatter is valid (--- delimiters, required fields)
  - Required sections are present (When To Use, Workflow, Output Format)
  - Knowledge references point to existing files
  - No broken internal links
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Optional, Tuple, List


REPO_ROOT = Path(__file__).resolve().parent.parent

SKILL_DIRS = [
    "skills/core",
    "skills/paradigms",
    "skills/languages",
    "skills/domains",
    "skills/frameworks",
    "skills/platforms",
]

REQUIRED_FRONTMATTER_FIELDS = ["name", "description"]
REQUIRED_SECTIONS = ["## When To Use", "## Workflow", "## Output Format"]


def find_all_skills() -> list[Path]:
    """Find all SKILL.md files in the repository."""
    skills = []
    for skill_dir in SKILL_DIRS:
        full_path = REPO_ROOT / skill_dir
        if not full_path.exists():
            continue
        for entry in sorted(full_path.rglob("SKILL.md")):
            skills.append(entry)
    return skills


def parse_frontmatter(content: str) -> Tuple[Optional[dict], str, List[str]]:
    """Parse YAML-like frontmatter from SKILL.md content.

    Returns (frontmatter_dict, body_text, errors).
    """
    errors = []
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        return None, content, ["Missing opening '---' frontmatter delimiter"]

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return None, content, ["Missing closing '---' frontmatter delimiter"]

    frontmatter_lines = lines[1:end_idx]
    body = "\n".join(lines[end_idx + 1:])

    frontmatter = {}
    for line in frontmatter_lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"^(\w+)\s*:\s*(.+)$", line)
        if match:
            key = match.group(1)
            value = match.group(2).strip().strip('"').strip("'")
            frontmatter[key] = value
        else:
            errors.append(f"Unparseable frontmatter line: {line}")

    return frontmatter, body, errors


def validate_skill(skill_path: Path) -> dict:
    """Validate a single SKILL.md file.

    Returns a dict with validation results.
    """
    result = {
        "path": str(skill_path),
        "name": skill_path.parent.name,
        "valid": True,
        "errors": [],
        "warnings": [],
    }

    if not skill_path.exists():
        result["valid"] = False
        result["errors"].append("File not found")
        return result

    try:
        content = skill_path.read_text(encoding="utf-8")
    except Exception as e:
        result["valid"] = False
        result["errors"].append(f"Cannot read file: {e}")
        return result

    # Check frontmatter
    frontmatter, body, fm_errors = parse_frontmatter(content)
    if fm_errors:
        result["errors"].extend(fm_errors)

    if frontmatter is not None:
        for field in REQUIRED_FRONTMATTER_FIELDS:
            if field not in frontmatter:
                result["errors"].append(f"Missing required frontmatter field: '{field}'")
    else:
        result["warnings"].append("No YAML frontmatter found (optional for some skills)")

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section not in content:
            result["warnings"].append(f"Missing recommended section: {section}")

    # Check knowledge references
    knowledge_refs = re.findall(r"knowledge/[\w/-]+", content)
    for ref in knowledge_refs:
        ref_path = REPO_ROOT / ref
        # Try with .md extension
        if not ref_path.exists() and not ref_path.with_suffix(".md").exists():
            result["warnings"].append(f"Knowledge reference may not exist: {ref}")

    # Check internal links
    internal_links = re.findall(r"\]\(([^)]+)\)", content)
    for link in internal_links:
        if link.startswith("http") or link.startswith("#"):
            continue
        link_path = (skill_path.parent / link).resolve()
        if not link_path.exists():
            result["warnings"].append(f"Broken internal link: {link}")

    if result["errors"]:
        result["valid"] = False

    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate Architecture Agent Skills."
    )
    parser.add_argument(
        "--skill",
        type=str,
        default=None,
        help="Validate only skills matching this name.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail (exit code 1) on warnings as well as errors.",
    )

    args = parser.parse_args()

    skills = find_all_skills()

    if args.skill:
        skills = [s for s in skills if args.skill.lower() in s.parent.name.lower()]

    if not skills:
        print("No skills found to validate.")
        sys.exit(0)

    results = [validate_skill(s) for s in skills]

    valid_count = sum(1 for r in results if r["valid"])
    error_count = sum(1 for r in results if r["errors"])
    warning_count = sum(1 for r in results if r["warnings"])

    if args.json:
        output = {
            "total": len(results),
            "valid": valid_count,
            "with_errors": error_count,
            "with_warnings": warning_count,
            "results": results,
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"Validated {len(results)} skill(s): {valid_count} valid, "
              f"{error_count} with errors, {warning_count} with warnings\n")

        for r in results:
            status = "✓" if r["valid"] else "✗"
            print(f"  {status}  {r['name']} ({r['path']})")
            for err in r["errors"]:
                print(f"       ERROR: {err}")
            for warn in r["warnings"]:
                print(f"       WARN:  {warn}")

        if error_count > 0:
            print(f"\n{error_count} skill(s) have errors.")
        if warning_count > 0 and args.strict:
            print(f"\n{warning_count} skill(s) have warnings (strict mode).")

    # Exit code
    has_failures = error_count > 0 or (args.strict and warning_count > 0)
    sys.exit(1 if has_failures else 0)


if __name__ == "__main__":
    main()
