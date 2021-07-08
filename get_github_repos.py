from github import Github
from sksurgerystats.common import add_github_package

token = None
with open("github.token", "r") as token_file:
    token = token_file.read()
    token = token.rstrip('\n')

if token is not None:
    g = Github(token)
    reps=g.search_repositories(query='scikit-surgery in:name')
    for rep in reps:
        add_github_package(rep)
