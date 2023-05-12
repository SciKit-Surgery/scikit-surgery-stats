"""
Searches for packages on pypi with SciKit-Surgery in the name, then 
gets some statistics for them
"""

import os.path
import urllib.request
import subprocess
import json
from datetime import datetime
import sksurgerystats.from_pypi as skspypi
from sksurgerystats.common import add_packages

#packages = os.system('./pypi-simple-search scikit-surgery')

if __name__ == '__main__':
    new_packages = skspypi.find_new_pypi_packages('scikit-surgery')
    add_packages(new_packages)
