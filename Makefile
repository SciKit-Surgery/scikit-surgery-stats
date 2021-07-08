#step 1 search for relevant packages on pypi and githib
python get_pypi_repos.py
python get_github_repos.py
#update stats for pypi
python update_pypi_stats.py
python update_github_stats.py
#what badges can we find
python get_badges.py
python update_dashboard.py
