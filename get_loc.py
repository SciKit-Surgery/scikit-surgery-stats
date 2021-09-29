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

def load_cache_file(filename):
    """Loads lines of code data from filename, stripping 
    var_name from the front
    """
    ret_dict = {}
    try:
        with open(filename, 'r') as filein:
            try:
                jsontext = filein.read().split('=')[1]
                ret_dict = json.loads(jsontext)
            except json.JSONDecodeError:
                raise json.JSONDecodeError
            except IndexError:
                raise IndexError
    except FileNotFoundError:
        pass

    return ret_dict


if __name__ == '__main__':
    packages = get_packages()
            
    for package in packages:
        
        print("Counting lines of ", package)

        homepage = get_package_information(package, 'home_page')
        
        cache_file = str('libraries/lines_of_code/' + package + '.js')

        git_hashes = load_cache_file(cache_file)

        temp_dir = '/dev/shm/sks_temp_for_cloc'
        if homepage is not None:
            if get_last_commit(homepage) in git_hashes:
                print("No need to update ", package, " skipping")
                continue
            shutil.rmtree(temp_dir, ignore_errors = True)
            subprocess.run(['git',  'clone', homepage, '/dev/shm/sks_temp_for_cloc'])
            commits = get_commits (temp_dir)
            for commit in commits:
                date = datetime.datetime.fromtimestamp(int(commit.split()[0].replace('"', '')))
                githash = commit.split()[1].replace('"', '')
                if githash not in git_hashes:
                    loc = get_loc(githash, temp_dir)
                    git_hashes[githash] = { 'loc' : loc , 'date' : date.isoformat() } 
                else:
                    print("hash " , githash, '  already present')
            outstring = str('var loc_data = ' + json.dumps( git_hashes))
            with open(cache_file, 'w') as fileout:
                fileout.write(outstring)
            exit()
        else:
            print (package , " has no homepage")

