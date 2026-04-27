#!/usr/bin/env node
/**
 * archskill — CLI for managing Architecture Agent Skills.
 *
 * Usage:
 *   archskill list                          List installed skills
 *   archskill install                       Install all skills to ~/.claude/skills/
 *   archskill install --skill <name>        Install a specific skill
 *   archskill install --project             Install to .claude/skills/ (project-local)
 *   archskill validate                      Validate all skills
 *   archskill validate --skill <name>       Validate a specific skill
 *   archskill validate --strict             Fail on warnings
 *   archskill new <name>                    Scaffold a new skill
 *
 * This CLI delegates to the Python scripts in scripts/.
 * Requires: Python 3.8+, Node.js 18+
 */

import { execSync } from "child_process";
import { existsSync, mkdirSync, writeFileSync } from "fs";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const REPO_ROOT = resolve(__dirname, "..");

const SCRIPTS = {
  install: resolve(REPO_ROOT, "scripts", "install_skill.py"),
  list: resolve(REPO_ROOT, "scripts", "list_skills.py"),
  validate: resolve(REPO_ROOT, "scripts", "validate_skills.py"),
};

function runPython(scriptPath, args = []) {
  const cmd = `python3 "${scriptPath}" ${args.join(" ")}`;
  try {
    const output = execSync(cmd, { cwd: REPO_ROOT, encoding: "utf-8", stdio: "pipe" });
    process.stdout.write(output);
  } catch (err) {
    if (err.stdout) process.stdout.write(err.stdout);
    if (err.stderr) process.stderr.write(err.stderr);
    process.exit(err.status || 1);
  }
}

function scaffoldSkill(name) {
  const skillPath = resolve(REPO_ROOT, "skills", "core", name);
  if (existsSync(skillPath)) {
    console.error(`Skill already exists: ${skillPath}`);
    process.exit(1);
  }

  mkdirSync(skillPath, { recursive: true });

  const skillMd = `---
name: ${name}
description: TODO: Describe what this skill does.
---

# ${name}

## When To Use

TODO: Describe the situation in which an agent should invoke this skill.

## Inputs To Inspect

- TODO: List the inputs the agent needs to inspect.

## Knowledge To Use

- TODO: Link to relevant knowledge cards.

## Workflow

1. TODO: Step 1
2. TODO: Step 2
3. TODO: Step 3

## Decision Rules

- TODO: List decision rules.

## Output Format

TODO: Describe the expected output format.

## Stop Conditions

- TODO: When should the agent stop?
`;

  const readmeMd = `# ${name}

TODO: Write a human-readable summary of this skill.
`;

  writeFileSync(resolve(skillPath, "SKILL.md"), skillMd, "utf-8");
  writeFileSync(resolve(skillPath, "README.md"), readmeMd, "utf-8");

  console.log(`Created skill: ${skillPath}`);
  console.log(`  ${skillPath}/SKILL.md`);
  console.log(`  ${skillPath}/README.md`);
}

function printHelp() {
  console.log(`
archskill — CLI for Architecture Agent Skills

Usage:
  archskill list                          List installed skills
  archskill install                       Install all skills to ~/.claude/skills/
  archskill install --skill <name>        Install a specific skill
  archskill install --project             Install to .claude/skills/ (project-local)
  archskill validate                      Validate all skills
  archskill validate --skill <name>       Validate a specific skill
  archskill validate --strict             Fail on warnings
  archskill new <name>                    Scaffold a new skill
  archskill --help                        Show this help
  archskill --version                     Show version
`);
}

function printVersion() {
  const pkg = JSON.parse(
    execSync(`cat "${resolve(REPO_ROOT, "package.json")}"`, { encoding: "utf-8" })
  );
  console.log(pkg.version);
}

function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args[0] === "--help" || args[0] === "-h") {
    printHelp();
    return;
  }

  if (args[0] === "--version" || args[0] === "-v") {
    printVersion();
    return;
  }

  const command = args[0];
  const commandArgs = args.slice(1);

  switch (command) {
    case "list":
      runPython(SCRIPTS.list, commandArgs);
      break;

    case "install":
      runPython(SCRIPTS.install, commandArgs);
      break;

    case "validate":
      runPython(SCRIPTS.validate, commandArgs);
      break;

    case "new":
      if (!commandArgs[0]) {
        console.error("Usage: archskill new <skill-name>");
        process.exit(1);
      }
      scaffoldSkill(commandArgs[0]);
      break;

    default:
      console.error(`Unknown command: ${command}`);
      console.error("Run 'archskill --help' for usage.");
      process.exit(1);
  }
}

main();
