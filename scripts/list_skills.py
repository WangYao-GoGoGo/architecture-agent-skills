#!/usr/bin/env python3
"""
list_skills.py — List installed Architecture Agent Skills.

Usage:
    python scripts/list_skills.py              # List globally installed skills
    python scripts/list_skills.py --project    # List project-local skills
    python scripts/list_skills.py --all        # List both global and project-local
    python scripts/list_skills.py --json       # Output as JSON

This script scans Claude Code skill directories and reports what's installed.
"""

import argparse
import json
import os
import sys
from pathlib import Path


CLAUDE_GLOBAL_DIR = Path.home() / ".claude" / "skills"
CLAUDE_PROJECT_DIR = Path.cwd() / ".claude" / "skills"


def scan_skills(directory: Path) -> list[dict]:
    """Scan a Claude Code skills directory and return installed skills.

    Returns a list of dicts with keys: name, category, path.
    """
    skills = []
    if not directory.exists():
        return skills

    for category_dir in sorted(directory.iterdir()):
        if not category_dir.is_dir():
            continue
        for skill_dir in sorted(category_dir.iterdir()):
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                skills.append({
                    "name": skill_dir.name,
                    "category": category_dir.name,
                    "path": str(skill_md),
                })
    return skills


def print_table(skills: list[dict], header: str) -> None:
    """Print skills in a formatted table."""
    if not skills:
        print(f"{header}: (none)")
        return

    print(f"\n{header}:")
    print(f"{'Category':<20} {'Skill':<40} {'Path'}")
    print("-" * 100)
    for s in sorted(skills, key=lambda x: (x["category"], x["name"])):
        print(f"{s['category']:<20} {s['name']:<40} {s['path']}")
    print(f"\nTotal: {len(skills)} skill(s)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="List installed Architecture Agent Skills."
    )
    parser.add_argument(
        "--project",
        action="store_true",
        help="List project-local skills (.claude/skills/).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        dest="show_all",
        help="List both global and project-local skills.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON.",
    )

    args = parser.parse_args()

    if args.show_all:
        global_skills = scan_skills(CLAUDE_GLOBAL_DIR)
        project_skills = scan_skills(CLAUDE_PROJECT_DIR)

        if args.json:
            print(json.dumps({
                "global": global_skills,
                "project": project_skills,
            }, indent=2))
        else:
            print_table(global_skills, "Global (~/.claude/skills/)")
            print_table(project_skills, "Project (.claude/skills/)")

    elif args.project:
        skills = scan_skills(CLAUDE_PROJECT_DIR)
        if args.json:
            print(json.dumps(skills, indent=2))
        else:
            print_table(skills, "Project-Local Skills (.claude/skills/)")

    else:
        skills = scan_skills(CLAUDE_GLOBAL_DIR)
        if args.json:
            print(json.dumps(skills, indent=2))
        else:
            print_table(skills, "Globally Installed Skills (~/.claude/skills/)")


if __name__ == "__main__":
    main()
