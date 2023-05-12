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
        get_package_information, get_packages
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
        packages = get_packages(sort_key = 'First Release Date')

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
            lines_of_code = get_package_information(package, 'loc')
           
            homepage = get_package_information(package, 'home_page')
            if homepage is None:
                homepage = 'Not Found'
            
            fileout.write('  <tr>\n')
           
            short_homepage = homepage
            host_logo = 'None'
            logo_spacer = ''
            try:
                short_homepage = homepage.split('/')[2]
                host_logo = short_homepage.split('.')[0]
                if host_logo == 'weisslab':
                    host_logo = 'gitlab'
            except:
                logo_spacer = '.%20%20%20'
                pass
            
            package_badge = str('https://img.shields.io/badge/' + logo_spacer +
                    str(count) + '-' + package.replace('-', '&#8209') +
                    '-orange?style=flat&logo=' + host_logo)
            WriteCellWithLinkedImage(fileout, package_badge , 
                    homepage, 'Library Homepage')
            
            weeks_up = 0
            try:
                time_up = datetime.now() - datetime.fromisoformat(first_release)
                weeks_up = int(time_up.days/7)
            except ValueError:
                pass
            
            weeks_up_badge = None
            weeks_up_target = None
            if weeks_up > 0:
                weeks_up_badge = str('https://img.shields.io/badge/Weeks%20Up-' + 
                    str(weeks_up) + '-green?style=flat')
                weeks_up_target = str(homepage + '/releases')

            WriteCellWithLinkedImage(fileout, weeks_up_badge, 
                    weeks_up_target, 'Total Weeks Up')
            
            last_release_badge = None
            last_release_target = None
            if last_release != 'n/a':
                last_release_badge = str('https://img.shields.io/badge/Last%20Release-' +
                    str(last_release).split('T')[0].replace('-', '%20') + '-green?style=flat') 
                last_release_target = str(homepage + '/releases')
            
            WriteCellWithLinkedImage(fileout, last_release_badge, 
                    last_release_target, 'Last Release Date')

            WriteCellWithLinkedImage(fileout, ci_badge, 
                    ci_target, 'CI Status')
            WriteCellWithLinkedImage(fileout, docs_badge, 
                    docs_target, 'Docs Status')
            WriteCellWithLinkedImage(fileout, coverage_badge, 
                    coverage_target, 'Code Coverage')

            loc_badge = None
            loc_link = str('loc/' + package + '.html')
            if lines_of_code is not None:
                loc_badge = str('https://img.shields.io/badge/LOC-' +
                    str(lines_of_code) + '-blue?style=flat')
             
            WriteCellWithLinkedImage(fileout, loc_badge, loc_link, 'Lines of Code')

            WriteCellWithLinkedImage(fileout, pepy_downloads_badge, 
                    pepy_downloads_target, 'All Downloads from PePy')

            github_user = get_package_information(package, 'GitHub User')
            stars_badge = None
            forks_badge = None
            watchers_badge = None
            contrib_badge = None
            if github_user is not None:
                stars_badge = str('https://img.shields.io/github/stars/' + github_user + '/' + package +
                    '?style=social')
                forks_badge = str('https://img.shields.io/github/forks/' + github_user + '/' + package +
                    '?style=social')
                watchers_badge = str('https://img.shields.io/github/watchers/' + github_user + '/' + package +
                    '?style=social')
                contrib_badge = str('https://img.shields.io/badge/contrib-' + 
                        str(contributors) 
                        + '-lightgrey?style=social&logo=github')

            WriteCellWithLinkedImage(fileout, stars_badge, 
                    str(homepage + '/stargazers'), 'GitHub Stars')
            
            WriteCellWithLinkedImage(fileout, forks_badge, 
                    str(homepage + '/forks'), 'GitHub Forks')
            
            WriteCellWithLinkedImage(fileout, watchers_badge, 
                    str(homepage + '/watchers'), 'GitHub Watchers')

            WriteCellWithLinkedImage(fileout, contrib_badge, 
                    str(homepage + '/graphs/contributors'), 'GitHub Contributors')
            
            WriteCellWithLinkedImage(fileout, syntek_package_health_badge, 
                    syntek_package_health_target, 'SynTek Package Health')
            
            WriteCellWithLinkedImage(fileout, codeclimate_badge, 
                    codeclimate_target, 'SynTek Package Health')

            fileout.write('  </tr>\n')
        

        fileout.write(tail)


    head = ""
    with open('html/excluded.html.in.head', 'r') as filein:
        head = filein.read()

    tail = ""
    with open('html/excluded.html.in.tail', 'r') as filein:
        tail = filein.read()

    with open('html/exclusions.html' , 'w') as fileout:
        fileout.write(head)

        excluded_packages = get_packages(sort_key = None, 
                                         path = 'libraries/exclusions/',
                                         exclusions_path = 'not a path')

        for new_count, package in enumerate(excluded_packages):
            homepage = get_package_information(package, 'home_page')
            if homepage is None:
                homepage = 'Not Found'
            
            fileout.write('  <tr>\n')
           
            short_homepage = homepage
            host_logo = 'None'
            logo_spacer = ''
            try:
                short_homepage = homepage.split('/')[2]
                host_logo = short_homepage.split('.')[0]
                if host_logo == 'weisslab':
                    host_logo = 'gitlab'
            except:
                logo_spacer = '.%20%20%20'
                pass
            
            package_badge = str('https://img.shields.io/badge/' + logo_spacer +
                    str(count+new_count+1) + '-' + package.replace('-', '&#8209') +
                    '-orange?style=flat&logo=' + host_logo)
            WriteCellWithLinkedImage(fileout, package_badge , 
                    homepage, 'Library Homepage')

            reason = get_package_information(package, 'obsolete', 
                                             path = 'libraries/exclusions/')
            fileout.write('    <td>\n')
            fileout.write('      <p>' + str(reason) + '</p>\n')
            fileout.write('    </td>\n')

            fileout.write('  </tr>\n')
   

        fileout.write(tail)


