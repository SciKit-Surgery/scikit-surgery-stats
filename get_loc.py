"""
Searches for packages on pypi with SciKit-Surgery in the name, then 
gets some statistics for them
"""
import requests
import os.path
import shutil
import urllib 
import subprocess
import json
import datetime
import subprocess
from github import Github, GithubException
from sksurgerystats.from_github import get_github_stats
from sksurgerystats.common import update_package_information, \
        get_package_information, get_packages

def get_loc(githash, directory="./"):
    current_dir = os.getcwd()
    os.chdir(directory)
    loc = subprocess.run(['cloc', githash, '--quiet'],
        capture_output=True).stdout
    total = loc.decode('utf-8').replace('-','').split()[-1]
    os.chdir(current_dir)
    return total

def get_commits(directory="./"):
    current_dir = os.getcwd()
    os.chdir(directory)
    commits = subprocess.run(['git', 'log', '--format="%ct %h"'], 
                capture_output=True).stdout
    commits = commits.decode('utf-8').splitlines()
    os.chdir(current_dir)
    return commits

def get_last_commit(project_name, token = None):
    github=Github(token)
    split_name = project_name.split('/')
    try:
        project_name = split_name[-2] + '/' + split_name[-1]
    except IndexError:
        pass
    
    rep=github.get_repo(project_name)
    default_branch = rep.get_branch(rep.default_branch)
    last_commit = default_branch.commit.sha[0:7]

    return last_commit

if __name__ == '__main__':
    packages = get_packages()
            
    for package in packages:
        
        print("Counting lines of ", package)

        homepage = get_package_information(package, 'home_page')
        
        cache_file = str('libraries/lines_of_code/' + package)

        git_hashes = []
        try:
            with open(cache_file, 'r') as filein:
                for line in filein.readlines():
                    if line[0] != '#':
                        git_hashes.append(line.split()[1])
        except FileNotFoundError:
            pass
        

        temp_dir = '/dev/shm/sks_temp_for_cloc'
        if homepage is not None:
            if get_last_commit(homepage) in git_hashes:
                print("No need to update ", package, " skipping")
                continue
            shutil.rmtree(temp_dir, ignore_errors = True)
            subprocess.run(['git',  'clone', homepage, '/dev/shm/sks_temp_for_cloc'])
            commits = get_commits (temp_dir)
            for commit in commits:
                date = datetime.date.fromtimestamp(int(commit.split()[0].replace('"', '')))
                githash = commit.split()[1].replace('"', '')
                if githash not in git_hashes:
                    if not os.path.isfile(cache_file):
                        with open(cache_file, 'w') as fileout:
                            fileout.write('#date hash lines_of_code')

                    with open(cache_file, 'a') as fileout:
                        loc = get_loc(githash, temp_dir)
                        fileout.write (str(date.isoformat() + ' ' + githash + ' ' + loc + '\n'))
                else:
                    print("hash " , githash, '  already present')
            exit()
        else:
            print (package , " has no homepage")

