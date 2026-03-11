m2ee-tools
==========

## ** M2EE-tools only support Debian 10 (buster) and Mendix Runtime versions 7-9. Further version support will not be added anymore. **

m2ee, the Mendix runtime helper tools for GNU/Linux

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

## Documentation

For further documentation, please refer to [the included documentation](doc/README.md)

m2ee-tools on github:
https://github.com/mendix/m2ee-tools/
