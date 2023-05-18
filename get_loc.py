"""
Searches for packages on pypi with SciKit-Surgery in the name, then 
gets some statistics for them
"""
import os.path
import shutil
import subprocess
import subprocess
from github import Github, GithubException
from sksurgerystats.html import load_cache_file, make_html_file, write_to_js_file
from sksurgerystats.from_github import get_github_stats, get_token, get_loc, get_last_commit
from sksurgerystats.common import update_package_information, \
        get_package_information, get_packages


if __name__ == '__main__':
    packages = get_packages()
        
    token = None
    token = get_token()

    #cleanup of temp directory if script couldn't complete the last time it was run 
    temp_dir = os.path.join(os.getcwd(), 'temp')
    shutil.rmtree(temp_dir, ignore_errors = True) 
    
    for package in packages:
        
        print("Counting lines of ", package)

        homepage = get_package_information(package, 'home_page')
        
        cache_file = str('libraries/lines_of_code/' + package + '.js')
        html_file = str('loc/' + package + '.html')
        if not os.path.exists(cache_file):
            continue
        git_hashes = load_cache_file(cache_file)
        last_hash = git_hashes if isinstance(git_hashes, str) else list(git_hashes.keys())[-1]
        
        if not os.path.exists(temp_dir):
            os.mkdir(temp_dir)
        if homepage is not None:
            try: 
                last_hash = get_last_commit(homepage, token)
                if get_last_commit(homepage, token) in git_hashes:
                    print("No need to update ", package, " skipping")
                    continue
            except:
                    subprocess.run(['git',  'clone', '--depth', '1', homepage, temp_dir]) 
                    last_loc = get_loc(last_hash, temp_dir)
                    update_package_information(package, 'loc', last_loc, overwrite = True) 
                    write_to_js_file(last_hash, cache_file)
                    make_html_file(package, cache_file)    
                    shutil.rmtree(temp_dir, ignore_errors = True)
        else:
            print (package , " has no homepage")
