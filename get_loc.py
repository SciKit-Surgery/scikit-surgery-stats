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
        current_dir = os.getcwd()
        if homepage is not None:
            os.chdir(current_dir)
            shutil.rmtree('/dev/shm/sks_temp_for_cloc', ignore_errors = True)
            subprocess.run(['git',  'clone', homepage, '/dev/shm/sks_temp_for_cloc'])

            os.chdir('/dev/shm/sks_temp_for_cloc')
            commits = subprocess.run(['git', 'log', '--format="%ct %h"'], 
                    capture_output=True).stdout
            for commit in commits.decode('utf-8').splitlines():
                date = commit.split()[0].replace('"', '')
                githash = commit.split()[1].replace('"', '')
                print ('Date:' , date, ' hash:', githash, end='')
                loc = subprocess.run(['cloc', githash, '--quiet'],
                    capture_output=True).stdout
                total = loc.decode('utf-8').replace('-','').split()[-1]
                print (" Sum = ", total)
            exit()
        else:
            print (package , " has no homepage")
        

            

