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
            fileout.write(str('      <p>' + first_release + '</p>\n')) 
            fileout.write('    </td>\n')

            fileout.write('    <td>\n')
            fileout.write(str('      <p>' + last_release + '</p>\n')) 
            fileout.write('    </td>\n')
            
            if ci_badge is None:
                ci_badge = "None"
            if ci_target is None:
                ci_target = ""
            fileout.write('    <td>\n')
            fileout.write(str('      <a href="' + ci_target + '">\n')) 
            fileout.write(str('        <img src="' + ci_badge + '" alt="CI Status">\n')) 
            fileout.write(str('      </a>\n')) 
            fileout.write('    </td>\n')

            fileout.write('  </tr>\n')


        fileout.write(tail)






