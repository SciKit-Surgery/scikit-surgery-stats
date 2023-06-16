"""
Checks that happens before the cookieninja generates the template

It checks the library_name in cookiecutter.json config file actually has valid characters
Then check if searching in pypi with the given base library name returns entries
"""

import re
import sys

import requests

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

library_name = "{{ cookiecutter.base_library_name }}"

response = requests.get(
    f"https://pypi.org/search/?q={library_name}&o=", timeout=20
)  # 20 seconds

if not re.match(MODULE_REGEX, library_name) or response.status_code != 200:
    print("ERROR: %s is not a valid Python module name!" % library_name)
    sys.exit(1)
