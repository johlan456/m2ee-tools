m2ee-tools
==========

CLI tool for deploying and managing [Mendix](https://www.mendix.com/) applications on GNU/Linux.

This is a maintained fork of the [original m2ee-tools](https://github.com/mendix/m2ee-tools/) by Mendix, which is no longer actively developed.

## Supported Versions

- **Mendix Runtime:** 7, 8, 9 (tested). Version 10+ may work but is not yet verified.
- **Python:** 3.8+
- **OS:** Any GNU/Linux distribution

## Installation

### Production

```sh
cd /opt/mendix/m2ee-tools  # or wherever the repo is cloned
pip install .
```

This installs the `m2ee` library and creates the `m2ee` CLI command on your PATH.

To update after pulling new changes:

```sh
git pull
pip install .
```

### Development

```sh
uv venv
uv pip install -e .
```

## Usage

```sh
m2ee          # Interactive REPL mode
m2ee -c stop  # Single command (non-interactive)
```

Configuration is read from `~/.m2ee/m2ee.yaml`. See [examples/](examples/) for reference configurations.

## Documentation

For detailed setup and configuration guides, see the [documentation](doc/README.md).

## License

BSD 3-Clause. See [LICENSE](LICENSE).
