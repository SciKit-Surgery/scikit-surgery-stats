"""
Searches for packages on pypi with SciKit-Surgery in the name, then 
gets some statistics for them
"""
import requests
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

            
    for package in packages:
        
        print("Getting badges for ", package)
        ci_badge = get_package_information(package, 'ci_badge')
        ci_target = get_package_information(package, 'ci_target')
        coverage_badge = get_package_information(package, 'coverage_badge')
        coverage_target = get_package_information(package, 'coverage_target')
        docs_badge = get_package_information(package, 'docs_badge')
        docs_target = get_package_information(package, 'docs_target')
        codeclimate_badge = get_package_information(package, 'codeclimate_badge')
        codeclimate_target = get_package_information(package, 'codeclimate_target')
        pepy_downloads_badge = get_package_information(package, 'pepy_downloads_badge')
        pepy_downloads_target = get_package_information(package, 'pepy_downloads_target')
        syntek_package_heath_badge = get_package_information(package, 'syntek_package_heath_badge')
        syntek_package_heath_target = get_package_information(package, 'syntek_package_heath_target')
        


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

            if docs_badge is None:
                docs_badge = str('https://readthedocs.org/projects/' + package + '/badge/?version=latest')
            if docs_target is None:
                docs_target = str('https://' + package + '.readthedocs.io/en/latest/?badge=latest')
                
            if codeclimate_badge is None:
                #doesn't seem a straight forward way here
                pass
            if codeclimate_target is None:
                codeclimate_target = str('https://codeclimate.com/github/' + project_name)

            if pepy_downloads_badge is None:
                pepy_downloads_badge = str('https://pepy.tech/badge/' + package)
            if pepy_downloads_target is None:
                pepy_downloads_target = str('https://pepy.tech/project' + package + '?branch=master')

            if syntek_package_heath_badge is None:
                syntek_package_heath_badge = str('https://snyk.io/advisor/python/' + package + '/badge.svg')
            if syntek_package_heath_target is None:
                syntek_package_heath_target = str('https://snyk.io/advisor/python/' + package)

        #check and update ci
        if ci_badge is not None:
            req=requests.get(ci_badge)
            if req.status_code == 200:
                update_package_information(package, 'ci_badge', ci_badge,
                        overwrite = True)
        
        if ci_target is not None:
            req=requests.get(ci_target)
            if req.status_code == 200:
                update_package_information(package, 'ci_target', ci_target,
                        overwrite = True)

        #cheek and update coverage
        if coverage_badge is not None:
            req=requests.get(coverage_badge)
            if req.status_code == 200:
                update_package_information(package, 'coverage_badge', coverage_badge,
                        overwrite = True)
        
        if coverage_target is not None:
            req=requests.get(coverage_target)
            if req.status_code == 200:
                update_package_information(package, 'coverage_target', coverage_target,
                        overwrite = True)

        #check and update docs
        if docs_badge is not None:
            req=requests.get(docs_badge)
            if req.status_code == 200:
                update_package_information(package, 'docs_badge', docs_badge,
                        overwrite = False)
        
        if docs_target is not None:
            req=requests.get(docs_target)
            if req.status_code == 200:
                update_package_information(package, 'docs_target', docs_target,
                        overwrite = True)

        #check and update codeclimate
        if codeclimate_badge is not None:
            req=requests.get(codeclimate_badge)
            if req.status_code == 200:
                update_package_information(package, 'codeclimate_badge', codeclimate_badge,
                        overwrite = True)
        
        if codeclimate_target is not None:
            req=requests.get(codeclimate_target)
            if req.status_code == 200:
                update_package_information(package, 'codeclimate_target', codeclimate_target,
                        overwrite = True)

        #check and update pepy_downloads
        if pepy_downloads_badge is not None:
            req=requests.get(pepy_downloads_badge)
            if req.status_code == 200:
                update_package_information(package, 'pepy_downloads_badge', pepy_downloads_badge,
                        overwrite = True)
        
        if pepy_downloads_target is not None:
            req=requests.get(pepy_downloads_badge)
            if req.status_code == 200:
                update_package_information(package, 'pepy_downloads_target', pepy_downloads_target,
                        overwrite = True)

        #check and update syntek_package_heath
        if syntek_package_heath_badge is not None:
            req=requests.get(syntek_package_heath_badge)
            if req.status_code == 200:
                update_package_information(package, 'syntek_package_heath_badge', syntek_package_heath_badge,
                        overwrite = True)
        
        if syntek_package_heath_target is not None:
            req=requests.get(syntek_package_heath_target)
            if req.status_code == 200:
                update_package_information(package, 'syntek_package_heath_target', syntek_package_heath_target,
                        overwrite = True)
