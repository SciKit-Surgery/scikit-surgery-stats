from github import Github

from sksurgerystats.common import add_github_package
from sksurgerystats.from_github import get_token

token = None
token = get_token()

if token is not None:
    g = Github(token)
    reps = g.search_repositories(
        query="{} in:name".format("{{ cookiecutter.base_library_name }}")
    )
    for rep in reps:
        add_github_package(rep)
