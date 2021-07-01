"""
Functions to get download data from pypi
"""
import subprocess
from pypinfo.cli import pypinfo

def get_existing_data(packagename, data_path = 'libraries/pypi-downloads/'):
    filename = str(data_path + packagename + '.downloads')
    months = []
    downloads = []
    try:
        with open(filename, 'r') as filein:
            for line in filein.readlines():
                if line[0] != '#':
                    months.append(line.split()[0])
                    downloads.append(line.split()[1])
    except FileNotFoundError:
        pass

    return months, downloads


def query_new_data(packagename, month, include_mirrors = False):
    subprocess.run(['pypinfo', '--auth', 'snappy-downloads-3d3fb7e245fd.json']) 
    download = subprocess.run(['pypinfo', '--month', month, packagename], capture_output=True).stdout


if __name__ == '__main__':
    months, downloads = get_existing_data('ndicapi')

    for i, month in enumerate(months):
        print('month: ', month, ' Downloads: ' , downloads[i])
