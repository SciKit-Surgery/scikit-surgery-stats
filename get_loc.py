"""
Searches for packages on pypi with SciKit-Surgery in the name, then 
gets some statistics for them
"""
import requests
import os.path
import shutil
import urllib 
import subprocess
import json
from datetime import datetime
import sksurgerystats.from_pypi as skspypi
from sksurgerystats.from_github import get_github_stats
from sksurgerystats.common import update_package_information, \
        get_package_information, get_packages

if __name__ == '__main__':
    packages = get_packages()
            
    for package in packages:
        
        print("Counting lines of ", package)

        homepage = get_package_information(package, 'home_page')
        if homepage is not None:
            shutil.rmtree('/dev/shm/sks_temp_for_cloc', ignore_errors = True)
            subprocess.run(['git',  'clone', homepage, '/dev/shm/sks_temp_for_cloc'])
            exit()
        else:
            print (package , " has no homepage")
        

            

