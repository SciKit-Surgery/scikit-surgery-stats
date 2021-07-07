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
    
    head = ""
    with open('html/dashboard.html.in.head', 'r') as filein:
        head = filein.read()
    
    tail = ""
    with open('html/dashboard.html.in.tail', 'r') as filein:
        tail = filein.read()

    with open('html/dashboard.html' , 'w') as fileout:
        fileout.write(head)
        
        all_packages = os.listdir('libraries/')
        packages = []
        for package in all_packages:
            if not os.path.isdir('libraries/' + package) and not \
                    package.endswith(".txt") and not \
                    package.startswith("."):
                packages.append(package)

        for package in packages:
            
            first_release = get_package_information(package, 'First Release Date')
            last_release = get_package_information(package, 'Last Release Date')
            stars = get_package_information(package, 'GitHub Stars')
            forks = get_package_information(package, 'GitHub Forks')
            watchers = get_package_information(package, 'GitHub Watchers')
            contributors = get_package_information(package, 'GitHub Contributors')
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
            if homepage is None:
                homepage = 'Not Found'
            
            fileout.write('  <tr>\n')
           
            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + package + '</p>\n')) 
            fileout.write('    </td>\n')
            
            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + 'description' + '</p>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + homepage + '</p>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + str(first_release).split('T')[0] + '</p>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + str(last_release).split('T')[0] + '</p>\n')) 
            fileout.write('    </td>\n')
            
            if ci_badge is None:
                ci_badge = "https://img.shields.io/badge/ci.yml-none-lightgrey"
            if ci_target is None:
                ci_target = ""
            fileout.write('    <td>\n')
            fileout.write(str('      <a href="' + ci_target + '">\n')) 
            fileout.write(str('        <img src="' + ci_badge + '" alt="CI Status">\n')) 
            fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')

            if docs_badge is None:
                docs_badge = "https://img.shields.io/badge/docs-none-lightgrey"
            if docs_target is None:
                docs_target = ""
            fileout.write('    <td>\n')
            fileout.write(str('      <a href="' + docs_target + '">\n')) 
            fileout.write(str('        <img src="' + docs_badge + '" alt="Docs Status">\n')) 
            fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')
            
            if coverage_badge is None:
                coverage_badge = "https://img.shields.io/badge/coverage-none-lightgrey"
            if coverage_target is None:
                coverage_target = ""
            fileout.write('    <td>\n')
            fileout.write(str('      <a href="' + coverage_target + '">\n')) 
            fileout.write(str('        <img src="' + coverage_badge + '" alt="Docs Status">\n')) 
            fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')

            if pepy_downloads_badge is None:
                pepy_downloads_badge = "https://img.shields.io/badge/pepy_downloads-none-lightgrey"
            if pepy_downloads_target is None:
                pepy_downloads_target = ""
            fileout.write('    <td>\n')
            fileout.write(str('      <a href="' + pepy_downloads_target + '">\n')) 
            fileout.write(str('        <img src="' + pepy_downloads_badge + '" alt="Docs Status">\n')) 
            fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + str(stars) + '</p>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + str(forks) + '</p>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + str(watchers) + '</p>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + str(contributors) + '</p>\n')) 
            fileout.write('    </td>\n')
            
            if syntek_package_heath_badge is None:
                syntek_package_heath_badge = "https://img.shields.io/badge/package_health-none-lightgrey"
            if syntek_package_heath_target is None:
                syntek_package_heath_target = ""
            fileout.write('    <td>\n')
            fileout.write(str('      <a href="' + syntek_package_heath_target + '">\n')) 
            fileout.write(str('        <img src="' + syntek_package_heath_badge + '" alt="Docs Status">\n')) 
            fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')
            
            if codeclimate_badge is None:
                codeclimate_badge = "https://img.shields.io/badge/codeclimate-none-lightgrey"
            if codeclimate_target is None:
                codeclimate_target = ""
            fileout.write('    <td>\n')
            fileout.write(str('      <a href="' + codeclimate_target + '">\n')) 
            fileout.write(str('        <img src="' + codeclimate_badge + '" alt="Docs Status">\n')) 
            fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')

            fileout.write('  </tr>\n')


        fileout.write(tail)





