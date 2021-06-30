from github import Github

token = None
with open("github.token", "r") as token_file:
    token = token_file.read()
    token = token.rstrip('\n')

if token is not None:
    g = Github(token)
    reps=g.search_repositories(query='scikit-surgery in:name')
    for i, rep in enumerate(reps):
        print(i, rep, rep.description)
        contibutors = 0 
        try:
            contibutors = len(rep.get_stats_contributors())
        except:
            pass


        print(i, rep, rep.stargazers_count, rep.watchers_count, rep.forks_count, contibutors)
