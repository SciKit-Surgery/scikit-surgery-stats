"""
Searches for packages on pypi with SciKit-Surgery in the name, then 
gets some statistics for them
"""

import os.path
import urllib 
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
        if not os.path.isdir('libraries/' + package) and not \
                package.endswith(".txt") and not \
                package.startswith("."):
            packages.append(package)

            ci_badge = get_package_information(package, 'ci_badge')
            ci_target = get_package_information(package, 'ci_target')
            coverage_badge = get_package_information(package, 'coverage_badge')
            coverage_target = get_package_information(package, 'coverage_target')


            homepage = get_package_information(package, 'home_page')
            if homepage is not None:
                
                project_name = homepage
                split_name = project_name.split('/')
                try:
                    project_name = split_name[-2] + '/' + split_name[-1]
                except IndexError:
                    pass

                if ci_badge is None:
                    ci_badge = str(homepage + '/workflows/.github/workflows/ci.yml/badge.svg')
                if ci_target is None:
                    ci_target = str(homepage + '/actions')
                if coverage_badge is None:
                    coverage_badge = str('https://coveralls.io/repos/github/' + project_name + '/badge.svg?branch=master&service=github')
                if coverage_target is None:
                    coverage_target = str('https://coveralls.io/github/' + project_name + '?branch=master')
                    
            req = urllib.request.Request(ci_badge)
            found_page = False
            try:
                urllib.request.urlopen(req)
                found_page = True
                update_package_information(package, 'ci_badge', ci_badge,
                        overwrite = True)
            except urllib.error.HTTPError:
                pass
            
            req = urllib.request.Request(ci_target)
            found_page = False
            try:
                urllib.request.urlopen(req)
                found_page = True
                update_package_information(package, 'ci_target', ci_target,
                        overwrite = True)
            except urllib.error.HTTPError:
                pass


            req = urllib.request.Request(coverage_badge)
            found_page = False
            try:
                urllib.request.urlopen(req)
                found_page = True
                update_package_information(package, 'coverage_badge', coverage_badge,
                        overwrite = True)
            except urllib.error.HTTPError:
                pass
          
            req = urllib.request.Request(coverage_target)
            found_page = False
            try:
                urllib.request.urlopen(req)
                found_page = True
                update_package_information(package, 'coverage_target', coverage_target,
                        overwrite = True)
            except urllib.error.HTTPError:
                pass






                 



   
