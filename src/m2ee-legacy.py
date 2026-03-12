#!/usr/bin/python3
#
# Legacy standalone script - kept for backward compatibility.
# New deployments should use: uv tool install git+https://github.com/johlan456/m2ee-tools
# which creates the 'm2ee' command automatically.
#
# This script simply delegates to m2ee.cli:main().
#

from m2ee.cli import main

if __name__ == '__main__':
    main()
