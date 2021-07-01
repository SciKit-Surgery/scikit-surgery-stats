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


def find_new_pypi_packages(searchname):
    """
    Searched for packages with names matching the searchname in PyPi
    """
    packages = subprocess.run(['./pypi-simple-search' , searchname], 
                    capture_output=True).stdout
    return packages.decode('utf-8').splitlines()

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

def get_release_information(package_dictionary):
    """
    Queries PyPi to get releases for each package
    returns the number of releases, first release date, 
    last release date, last release name
    """
    releases = package_dictionary.get('releases')
    releases_list = list(package_dictionary.get('releases'))
    first_release_date = None
    last_release_date = None
    last_release_name = None
    number_of_releases = len(releases_list)

    for release in releases_list:
        print(release, end = " ")
        release_date_string = releases.get(release)[0].get('upload_time')
        release_date = datetime.fromisoformat(release_date_string)
        if first_release_date is None:
            first_release_date = release_date
        if last_release_date is None:
            last_release_date = release_date

        if release_date < first_release_date:
            first_release_date = release_date
        if release_date > last_release_date:
            last_release_date = release_date
            last_release_name = release


        #release_date = datetime.strptime(release_date_string, 'iso')
        print(release_date)
    return number_of_releases, first_release_date, last_release_date,\
                   last_release_name

def get_json_from_pypi(package):
    """
    gets data on the package from pypi
    """
    url = str('https://pypi.org/pypi/' + package + '/json')
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    return json.loads(data)

if __name__ == '__main__':
    new_packages = find_new_pypi_packages('scikit-surgery')
    #add_packages(new_packages)
    packages = os.listdir('libraries/')
    for package in packages:
        if os.path.isdir(package) or package.endswith(".txt"):
            packages.remove(package)
    
    package_dictionaries = []
    for package in packages:
        package_dictionaries.append(get_json_from_pypi(package))

    for dictionary in package_dictionaries:
        print("getting releases for ", dictionary.get('info').get('name'))
        print(get_release_information(dictionary))


   
