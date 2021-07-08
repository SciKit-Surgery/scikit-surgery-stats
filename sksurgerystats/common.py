"""
Searches for packages on pypi with SciKit-Surgery in the name, then 
gets some statistics for them
"""

import os.path
import urllib.request
import subprocess
import json
from datetime import datetime

#packages = os.system('./pypi-simple-search scikit-surgery')

def add_packages(packages, path = 'libraries/'):
    """
    Searches through path directory for marker files
    for each package in list, creates file if not already present
    """
    for package in packages:
        filename = str('libraries/' + package)
        if not os.path.isfile(filename):
            print("Found new package ", package)
            with open(filename, 'w'):
                pass

def add_github_package(github_rep, path = 'libraries/'):
    """
    Searches through path directory for marker files
    for the package, creates file if not already present
    and writes home_page entry
    """
    filename = str('libraries/' + github_rep.name)
    if not os.path.isfile(filename):
        print("Found new package ", github_rep.full_name)
        with open(filename, 'w') as fileout:
            configuration = {'home_page' : github_rep.html_url}
            json.dump(configuration, fileout)


def update_package_information(package, key, entry, 
        overwrite = False, path='libraries/'):
    """
    adds key and entry to a dictionary for the given package.
    If overwrite is false it will not overwrite existing 
    entries
    """
    filename = str('libraries/' + package)
    configuration = None
    with open(filename, 'r') as filein:
        try:
            configuration = json.load(filein)
        except json.JSONDecodeError:
            configuration = {}

    if configuration.get(key, None) is None:
        configuration[key] = entry
    else:
        if overwrite:
            configuration[key] = entry
    
    with open(filename, 'w') as fileout:
        configuration = json.dump(configuration, fileout)
    
def get_package_information(package, key, path='libraries/'):
    """
    returns a key value for a given package, returns None
    if key not present
    """
    filename = str('libraries/' + package)
    configuration = None
    with open(filename, 'r') as filein:
        try:
            configuration = json.load(filein)
        except json.JSONDecodeError:
            configuration = {}
    
    return configuration.get(key, None)


