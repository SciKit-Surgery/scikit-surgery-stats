#step 1 search for relevant packages on pypi and githib
python get_pypi_repos.py
python get_github_repos.py
#update stats 
python update_pypi_stats.py
python update_github_stats.py
#get coverage/docs/etc badges
python get_badges.py
#update html files
python update_dashboard.py
