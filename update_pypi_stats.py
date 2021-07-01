"""
Searches for packages on pypi with SciKit-Surgery in the name, then 
gets some statistics for them
"""

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
                print("got " , package_data)

        except(FileNotFoundError):
            with open (filename, 'w') as write_file:
                json.dump({ 'name' : package }, write_file)

if __name__ == '__main__':
    packages = find_new_pypi_packages('scikit-surgery')
    init_packages(packages)

   
