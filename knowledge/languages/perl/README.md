# Perl Architecture Idioms

## Use When

- Reviewing Perl module design, CPAN dependency management, or text processing pipeline architecture.

## Heuristics

- Use `use strict; use warnings;` in every script and module.
- Prefer `Moose` or `Moo` for object-oriented code over bare `bless`.
- Organize code into `.pm` modules under `lib/` with proper package namespaces.
- Use `Exporter` or `Sub::Exporter` for selective function export.
- Use `CPANfile` or `cpanm` for dependency management.
- Prefer modern Perl features (`say`, `state`, `given`/`when`) from `use feature`.
- Use `Test::More` for unit testing — aim for comprehensive test coverage.
- Use `Path::Tiny` for file operations — it's safer than raw `open`.

## Common Risks

- Over-relying on `$_` implicit variable — it makes code hard to read.
- Using bare `open` without three-argument form and error checking.
- Global state from package variables (`our`) leaking across modules.
- Over-using regex for parsing structured data (HTML, JSON, etc.).
- Memory leaks from circular references in blessed references.
