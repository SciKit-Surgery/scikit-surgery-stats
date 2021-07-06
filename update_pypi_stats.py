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
from sksurgerystats.common import add_packages, update_package_information

if __name__ == '__main__':
    all_packages = os.listdir('libraries/')
    packages = []
    for package in all_packages:
        if not os.path.isdir('libraries/' + package) and not package.endswith(".txt"):
            packages.append(package)
    
    package_dictionaries = []
    for package in packages:
        package_dictionaries.append(skspypi.get_json_from_pypi(package))

    for dictionary in package_dictionaries:
        package_name = dictionary.get('info').get('name')
        print("getting releases for ", package_name)
        number_of_releases, first_release_date, last_release_date,\
                   last_release_name = \
                   skspypi.get_release_information(dictionary)
        print(number_of_releases, first_release_date, last_release_date,\
                   last_release_name)

        update_package_information(package_name, 'Number of Releases', 
                number_of_releases, 
                overwrite = True)


   
