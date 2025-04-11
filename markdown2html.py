#!/usr/bin/env python3

"""
Script to convert markdown to HTML
Usage: ./markdown2html.py README.md README.html
"""

import sys
import os


def main():
    # Check number of arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    # Get arguments
    md_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if markdown file exists
    if not os.path.exists(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
        sys.exit(1)

    # Here you would implement the conversion from markdown to HTML
    # For now, this script just satisfies the basic requirements

    # Exit with success status
    sys.exit(0)


if __name__ == "__main__":
    main()
