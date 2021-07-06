from github import Github

def get_github_stats(project_name):
    """ Get in formatation from github. project name can either be
    the github project name or the web address
    """
    split_name = project_name.split('/')
    project_name = split_name[-2] + '/' + split_name[-1]
    github = Github()
    rep=github.get_repo(project_name)
    print(rep, rep.description)
    contibutors = 0 
    try:
        contibutors = len(rep.get_stats_contributors())
    except:
        pass


    print(rep, rep.stargazers_count, rep.watchers_count, rep.forks_count, contibutors)
