"""
Searches for packages on pypi with SciKit-Surgery in the name, then 
gets some statistics for them
"""

import urllib.request
import subprocess
import json

#packages = os.system('./pypi-simple-search scikit-surgery')


def find_new_pypi_packages(searchname):
    """
    Searched for packages with names matching the searchname in PyPi
    """
    packages = subprocess.run(['./pypi-simple-search' , searchname], 
                    capture_output=True).stdout
    return packages.decode('utf-8').splitlines()

def init_packages(packages, path = 'libraries/'):
    """
    Searches through path directory for json files
    for each package in list, creates file if not already present
    """

    for package in packages:
        filename = str('libraries/' + package + '.json')
        try:
            with open (filename, 'r') as read_file:
                package_data = json.load(read_file)

        except(FileNotFoundError):
            with open (filename, 'w') as write_file:
                json.dump({ 'name' : package }, write_file)

def get_releases(packages):
    """
    Queries PyPi to get releases for each package
    """
    for package in packages:
        print("getting releases for ", package)
        url = str('https://pypi.org/pypi/' + package + '/json')
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        data = response.read()
        values = json.loads(data)
        releases = values.get('releases')
        releases_list = list(values.get('releases'))
        print(str(next(iter(releases))))
        for release in releases_list:
            print(release, end = " ")
            release_date = releases.get(release)[0].get('upload_time')
            print(release_date)
            #print (values.get('releases'))


if __name__ == '__main__':
    packages = find_new_pypi_packages('scikit-surgery')
    init_packages(packages)
    get_releases(packages)

   
