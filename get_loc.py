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
from sksurgerystats.from_github import get_github_stats, get_token
from sksurgerystats.common import update_package_information, \
        get_package_information, get_packages

def get_loc(githash, directory="./"):
    current_dir = os.getcwd()
    os.chdir(directory)
    loc = subprocess.run(['cloc', githash, '--quiet'],
        capture_output=True).stdout
    
    total = 0
    try: 
        total = loc.decode('utf-8').replace('-','').split()[-1]
    except IndexError:
        pass

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

def make_html_file(package, jsfile, 
        template_file = 'templates/loc_plot.html'):

    #create dir if not existing
    try:
        os.mkdir('loc/')
    except FileExistsError:
        pass

    with open(template_file, 'r') as filein:
        template = filein.read()

    with_title = template.replace('PAGE_TITLE', str(package + ' Lines of Code'))
    with_heading = with_title.replace('CHART_HEADING', str(package + ' Lines of Code vs Date'))
    with_data = with_heading.replace('PATH_TO_DATA', str('../' + jsfile))

    with open(str('loc/' + package + '.html'), 'w') as fileout:
        fileout.write(with_data)

def get_loc_by_commit(temp_dir, existing_commit):
    commits = get_commits(temp_dir)
    for commit in commits:
        date = datetime.datetime.fromtimestamp(int(commit.split()[0].replace('"', '')))
        githash = commit.split()[1].replace('"', '')
        if githash not in existing_commits:
            loc = get_loc(githash, temp_dir)
            existing_commits[githash] = { 'loc' : loc , 'date' : date.isoformat() } 
        else:
            print("hash " , githash, '  already present')

    return existing_commits

def write_to_js_file(data, fileout):

    outstring = str('var loc_data = ' + json.dumps(data))
    with open(fileout, 'w') as fileout:
        fileout.write(outstring)


if __name__ == '__main__':
    packages = get_packages()
        
    token = None
    token = get_token()

    for package in packages:
        
        print("Counting lines of ", package)

        homepage = get_package_information(package, 'home_page')
        
        cache_file = str('libraries/lines_of_code/' + package + '.js')
        html_file = str('loc/' + package + '.html')
        if not os.path.exists(cache_file):
            continue
        git_hashes = load_cache_file(cache_file)
        last_hash = git_hashes[list(git_hashes)[-1]]
        
        temp_dir = os.path.join(os.getcwd(), 'temp')
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        if homepage is not None:
            try:
                if get_last_commit(homepage, token) in git_hashes:
                    print("No need to update ", package, " skipping")
                    last_loc = last_hash['loc']
                    update_package_information(package, 'loc', last_loc, overwrite = False) 
                    continue
            except GithubException:
                pass

            shutil.rmtree(temp_dir, ignore_errors = True)
            subprocess.run(['git',  'clone', '--depth', '1', homepage, temp_dir]) 
            last_loc = get_loc_by_commit(temp_dir, last_hash)['loc']
           
            update_package_information(package, 'loc', last_loc, overwrite = True) 
            write_to_js_file(last_hash, cache_file)
            make_html_file(package, cache_file)
        else:
            print (package , " has no homepage")

