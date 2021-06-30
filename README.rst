scikit-surgery-stats
====================

This is a set of scripts to get statistics on the scikit-surgery library
and turn them into a nice webpage

::

    mkdir env
    python -m venv env/
    source env/bin/activate
    pip install -r requirements

    ./pypi-simple-search scikit-surgery > scikit-surgery-onpypi.txt

    python get_github_repos.py > scikit-surgery-ongithub.txt                                                                    

We can use pypinfo to get data for things on pypi

::
    pypinfo --auth snappy-downloads-3d3fb7e245fd.json
    pypinfo scikit-surgeryvtk country
~           
