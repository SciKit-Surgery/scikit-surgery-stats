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
from sksurgerystats.html import WriteCellWithLinkedImage

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

        for count, package in enumerate(packages):
            
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
            syntek_package_health_badge = get_package_information(package, 'syntek_package_heath_badge')
            syntek_package_health_target = get_package_information(package, 'syntek_package_heath_target')
            
            homepage = get_package_information(package, 'home_page')
            if homepage is None:
                homepage = 'Not Found'
            
            fileout.write('  <tr>\n')
           
            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + str(count) + '</p>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + package + '</p>\n')) 
            fileout.write('    </td>\n')
            
            short_homepage = homepage
            try:
                short_homepage = homepage.split('/')[2]
            except:
                pass

            fileout.write('    <td>\n')
            fileout.write(str('      <a href="' + homepage + '">\n'))
            fileout.write(str('        ' + short_homepage + '\n')) 
            fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + str(first_release).split('T')[0] + '</p>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + str(last_release).split('T')[0] + '</p>\n')) 
            fileout.write('    </td>\n')
            
            if ci_badge is None:
                ci_badge = "https://img.shields.io/badge/ci.yml-none-lightgrey?style=flat&logo=github"
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
           
            github_user = get_package_information(package, 'GitHub User')
            if github_user is not None:
                stars_badge = str('https://img.shields.io/github/stars/' + github_user + '/' + package +
                    '?style=social')
            else:
                stars_badge = str('https://img.shields.io/badge/stars-na-lightgrey?style=social&logo=github')

            fileout.write('    <td>\n')
            if github_user is not None:
                fileout.write(str('      <a href="' + homepage + '/stargazers">\n')) 
                fileout.write(str('        <img src="' + stars_badge + '" alt="Github Stars">\n')) 
                fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')
            
            if github_user is not None:
                forks_badge = str('https://img.shields.io/github/forks/' + github_user + '/' + package +
                    '?style=social')
            else:
                forks_badge = str('https://img.shields.io/badge/forks-na-lightgrey?style=social&logo=github')

            fileout.write('    <td>\n')
            if github_user is not None:
                fileout.write(str('      <a href="' + homepage + '/forks">\n')) 
                fileout.write(str('        <img src="' + forks_badge + '" alt="Github Forks">\n')) 
                fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')
            
            if github_user is not None:
                watchers_badge = str('https://img.shields.io/github/watchers/' + github_user + '/' + package +
                    '?style=social')
            else:
                watchers_badge = str('https://img.shields.io/badge/watchers-na-lightgrey?style=social&logo=github')

            fileout.write('    <td>\n')
            if github_user is not None:
                fileout.write(str('      <a href="' + homepage + '/watchers">\n')) 
                fileout.write(str('        <img src="' + watchers_badge + '" alt="Github Watchers">\n')) 
                fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')
            
            contrib_badge = None
            if github_user is not None: 
                contrib_badge = str('https://img.shields.io/badge/contrib-' + 
                        str(contributors) 
                        + '-lightgrey?style=social&logo=github')

            WriteCellWithLinkedImage(fileout, contrib_badge, 
                    str(homepage + '/graphs/contributors'), 'GitHub Contributors')
            
            WriteCellWithLinkedImage(fileout, syntek_package_health_badge, 
                    syntek_package_health_target, 'SynTek Package Health')
            
            WriteCellWithLinkedImage(fileout, codeclimate_badge, 
                    codeclimate_target, 'SynTek Package Health')

            fileout.write('  </tr>\n')


        fileout.write(tail)






