"""
Searches for packages on pypi with SciKit-Surgery in the name, then
gets some statistics for them
"""

import os.path
import urllib.request
from sksurgerystats.from_github import get_github_stats, get_token
from sksurgerystats.common import update_package_information, \
        get_package_information

if __name__ == '__main__':
    all_packages = os.listdir('libraries/')
    packages = []
    for package in all_packages:
        if not os.path.isdir('libraries/' + package) and not \
                package.endswith(".txt") and not \
                package.startswith("."):
            packages.append(package)

    token = None
    token = get_token()

    package_dictionaries = []
    for package in packages:
        homepage = get_package_information(package, 'home_page')

        if homepage is not None:
            rep, stars, watchers, forks, contributors = get_github_stats(homepage, token)

            update_package_information(package, 'GitHub Stars',
                    stars, overwrite = True)
            update_package_information(package, 'GitHub Watchers',
                    watchers, overwrite = True)
            update_package_information(package, 'GitHub Forks',
                    forks, overwrite = True)
            update_package_information(package, 'GitHub Contributors',
                    contributors, overwrite = True)
            try:
                update_package_information(package, 'GitHub User',
                        rep.organization.login, overwrite = True)
            except AttributeError:
                try:
                    update_package_information(package, 'GitHub User',
                        rep.owner.login, overwrite = True)
                except:
                    pass
            except:
                pass
