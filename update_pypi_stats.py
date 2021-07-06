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
from sksurgerystats.from_github import get_github_stats
from sksurgerystats.common import add_packages, update_package_information, \
        get_package_information

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
        number_of_releases, first_release_date, last_release_date,\
                   last_release_name = \
                   skspypi.get_release_information(dictionary)

        update_package_information(package_name, 'Number of Releases', 
                number_of_releases, 
                overwrite = True)
        
        update_package_information(package_name, 'First Release Date', 
                first_release_date, 
                overwrite = True)
        
        update_package_information(package_name, 'Last Release Date', 
                last_release_date, 
                overwrite = True)
        
        update_package_information(package_name, 'Last Release Name', 
                last_release_name, 
                overwrite = True)
    
        homepage = get_package_information(package_name, 'home_page')
        homepage = dictionary.get('info').get('home_page', homepage)
        print ("Got homepage", homepage)
        if homepage is not None:
            print(homepage)
            get_github_stats(homepage)
                 



   
