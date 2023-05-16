from github import Github, GithubException
from os import environ

def get_token():
    """ Get github personal access token. This function checks if the environment variable 
        added as secret.ADMIN_TOKEN exists (ex. inside a GHA) or a local github.token
        file exists, and returns whichever token exists.
    """
    if environ.get('admin_token') is not None:
        token = environ.get('admin_token')
    else:
        with open("github.token", "r") as token_file:
            token = token_file.read()
            token = token.rstrip('\n')
    return token
        
def get_github_stats(project_name, token = None):
    """ Get in formatation from github. project name can either be
    the github project name or the web address
    """
    rep = "not found"
    stars = 0 
    watchers = 0
    forks = 0 
    contributors = 0

    split_name = project_name.split('/')
    try:
        project_name = split_name[-2] + '/' + split_name[-1]
    except IndexError:
        pass

    github = Github(token)

    try:
        rep=github.get_repo(project_name)
    except GithubException:
        return rep, stars, watchers, forks, contributors
    try:
        contributors = len(rep.get_stats_contributors())
    except:
        pass
    
    stars = rep.stargazers_count
    watchers = rep.watchers_count
    forks = rep.forks_count

    return rep, stars, watchers, forks, contributors
