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
    filename = str(path + package)
    configuration = None
    with open(filename, 'r') as filein:
        try:
            configuration = json.load(filein)
        except json.JSONDecodeError:
            configuration = {}

    return configuration.get(key, None)


def get_packages(sort_key = None, path = 'libraries/',
        exclusions_path = 'libraries/exclusions/'):
    """
    returns a list of of packages, and optionally sorts by
    the sort key
    """
    all_packages = os.listdir(path)
    packages = []
    for package in all_packages:
        if not os.path.isdir(path + package) and not \
                package.endswith(".txt") and not \
                package.startswith(".") and not \
                os.path.isfile(exclusions_path + package):

            packages.append(package)

    if sort_key is None:
        return packages

    package_dictionaries = []
    for package in packages:
        package_dictionaries.append(
                {"package" : package,
                 "sort key" : get_package_information(package, sort_key, path)})
        if get_package_information(package, sort_key, path) is None:
            print(package + " sort key is None ", sort_key)

    sorted_dicts = sorted(package_dictionaries, key=lambda k: k['sort key'])

    packages = []
    for sorted_dict in sorted_dicts:
        packages.append(sorted_dict.get('package'))

    return packages



