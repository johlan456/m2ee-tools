# m2ee-tools

CLI tool for managing Mendix application deployments on GNU/Linux. Written in Python 3.

## Project Structure

```
src/m2ee.py          # Main CLI entry point (cmd.Cmd-based interactive shell)
src/m2ee/            # Core library package
  core.py            # M2EE class - runtime lifecycle management
  config.py          # YAML configuration parsing/validation
  client.py          # HTTP client for Mendix Admin API (JSON-RPC)
  runner.py          # JVM process management, PID tracking, signals
  version.py         # MXVersion semantic version comparison
  pgutil.py          # PostgreSQL utilities (backup, restore, sync)
  munin.py           # Munin monitoring integration
  nagios.py          # Nagios monitoring integration
  util.py            # Archive unpacking, symlink management
  smaps.py           # Linux /proc/smaps memory analysis
  exceptions.py      # M2EEException with error codes
  client_errno.py    # CLI exit state codes
examples/            # YAML configuration examples
doc/                 # Documentation (install, configure, nginx, security, monitoring)
munin/               # Munin plugin script
```

## Development

- **Python 3 only** (Python 2 dropped in v8.0)
- **Dependencies:** `requests`, `pyyaml`, `psycopg2` (optional, for PostgreSQL)
- **Packaging:** `setup.py` with setuptools
- **No test suite** currently in place

### Install for development

```sh
uv pip install -e .
```

### Run

```sh
m2ee          # Interactive REPL mode
m2ee -c stop  # Single command (non-interactive)
```

## Code Conventions

- snake_case for functions and variables, UPPER_CASE for constants
- 4-space indentation
- No type hints (legacy codebase)
- Custom TRACE log level (5) added via monkeypatch in `src/m2ee/__init__.py`
- CLI commands follow `do_<command>` pattern from `cmd.Cmd`
- Configuration loaded from `~/.m2ee/m2ee.yaml` (YAML, use `yaml.safe_load`)

## Git Workflow

- **Main branch:** `master`
- **Versioning:** semantic tags (e.g., `v8.0.1`)
- Project is in maintenance mode — bug fixes only, no new Mendix version support

## Key Patterns

- Mendix Admin API communication via HTTP JSON-RPC on localhost admin port
- PID file-based process tracking for the JVM runtime
- Configuration is mutable (reload without restart via `reload` command)
- Supports both interactive REPL and non-interactive (`-c` flag) modes

## Gotchas

- `setup.py` uses deprecated `distutils.core` — may need migration to pure setuptools for Python 3.12+
- Always use `yaml.safe_load()`, never `yaml.load()` — security requirement
- Non-TTY stdout (e.g. systemd): Python 3 handles encoding natively, do not wrap with `codecs.getwriter()`
- Version string lives in `src/m2ee/__init__.py` (`__version__`)
