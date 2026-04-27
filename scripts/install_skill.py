#!/usr/bin/env python3
"""
install_skill.py — Install Architecture Agent Skills into Claude Code.

Usage:
    python scripts/install_skill.py                     # Install all core skills
    python scripts/install_skill.py --skill runtime-error-diagnosis  # Install a specific skill
    python scripts/install_skill.py --project            # Install in .claude/skills/ (project-local)
    python scripts/install_skill.py --list               # List available skills
    python scripts/install_skill.py --dry-run            # Show what would be installed

This script copies SKILL.md files from skills/ into the Claude Code skills directory.
Global install:  ~/.claude/skills/
Project install: .claude/skills/  (relative to project root)
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Optional


REPO_ROOT = Path(__file__).resolve().parent.parent

# Directories that contain skills
SKILL_DIRS = [
    "skills/core",
    "skills/paradigms",
    "skills/languages",
    "skills/domains",
    "skills/frameworks",
    "skills/platforms",
]

# Claude Code skill paths
CLAUDE_GLOBAL_DIR = Path.home() / ".claude" / "skills"
CLAUDE_PROJECT_DIR = Path.cwd() / ".claude" / "skills"


def discover_skills() -> list[dict]:
    """Discover all skills in the repository.

    Returns a list of dicts with keys: name, path, category, description.
    """
    skills = []
    for skill_dir in SKILL_DIRS:
        full_path = REPO_ROOT / skill_dir
        if not full_path.exists():
            continue
        for entry in sorted(full_path.iterdir()):
            if not entry.is_dir():
                continue
            skill_md = entry / "SKILL.md"
            if not skill_md.exists():
                continue
            description = extract_description(skill_md)
            skills.append({
                "name": entry.name,
                "path": str(skill_md),
                "category": skill_dir.replace("skills/", ""),
                "description": description,
            })
    return skills


def extract_description(skill_md: Path) -> str:
    """Extract the description from a SKILL.md file."""
    try:
        content = skill_md.read_text(encoding="utf-8")
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("description:"):
                return line[len("description:"):].strip().strip('"').strip("'")
            if line.startswith("# "):
                # Fallback: use the first heading after frontmatter
                continue
        return ""
    except Exception:
        return ""


def install_skill(skill: dict, target_dir: Path, dry_run: bool = False) -> bool:
    """Install a single skill into the target directory.

    Returns True if installed, False if skipped.
    """
    src = Path(skill["path"])
    if not src.exists():
        print(f"  [SKIP]  {skill['name']} — source not found: {src}")
        return False

    dest = target_dir / skill["category"] / skill["name"] / "SKILL.md"
    if dry_run:
        print(f"  [DRY]   {skill['name']} -> {dest}")
        return True

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    print(f"  [OK]    {skill['name']} -> {dest}")
    return True


def install_all_skills(
    target_dir: Path,
    skill_filter: Optional[str] = None,
    dry_run: bool = False,
) -> int:
    """Install all (or filtered) skills into target_dir.

    Returns the count of installed skills.
    """
    skills = discover_skills()
    if not skills:
        print("No skills found in repository.")
        return 0

    if skill_filter:
        skills = [s for s in skills if skill_filter.lower() in s["name"].lower()]
        if not skills:
            print(f"No skills match filter: {skill_filter}")
            print(f"Available skills: {', '.join(s['name'] for s in discover_skills())}")
            return 0

    count = 0
    for skill in skills:
        if install_skill(skill, target_dir, dry_run):
            count += 1

    return count


def list_skills() -> None:
    """Print all available skills grouped by category."""
    skills = discover_skills()
    if not skills:
        print("No skills found.")
        return

    by_category: dict[str, list[dict]] = {}
    for s in skills:
        by_category.setdefault(s["category"], []).append(s)

    for category in sorted(by_category):
        print(f"\n{category}/")
        for s in by_category[category]:
            desc = f" — {s['description']}" if s["description"] else ""
            print(f"  {s['name']}{desc}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Install Architecture Agent Skills into Claude Code."
    )
    parser.add_argument(
        "--skill",
        type=str,
        default=None,
        help="Install only skills matching this name (case-insensitive substring match).",
    )
    parser.add_argument(
        "--project",
        action="store_true",
        help="Install in .claude/skills/ (project-local) instead of ~/.claude/skills/.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available skills and exit.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be installed without copying files.",
    )
    parser.add_argument(
        "--global",
        dest="global_install",
        action="store_true",
        help="Explicitly install to ~/.claude/skills/ (default).",
    )

    args = parser.parse_args()

    if args.list:
        list_skills()
        return

    target_dir = CLAUDE_PROJECT_DIR if args.project else CLAUDE_GLOBAL_DIR

    if args.dry_run:
        print(f"Dry run — target: {target_dir}")
    else:
        print(f"Installing skills to: {target_dir}")

    count = install_all_skills(target_dir, args.skill, args.dry_run)

    if not args.dry_run:
        print(f"\nInstalled {count} skill(s).")
        print(f"Target directory: {target_dir}")
        print("Restart Claude Code or reload skills to use them.")
    else:
        print(f"\nWould install {count} skill(s).")


if __name__ == "__main__":
    main()
