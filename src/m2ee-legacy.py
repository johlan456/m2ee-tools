#!/usr/bin/python3
#
# Legacy standalone script - kept for backward compatibility.
# New deployments should use: pip install . (or uv pip install .)
# which creates the 'm2ee' command via the entry point in pyproject.toml.
#
# This script simply delegates to m2ee.cli:main().
#

from m2ee.cli import main

if __name__ == '__main__':
    main()
