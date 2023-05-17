scikit-surgery-stats
====================

.. image:: https://img.shields.io/twitter/url?style=social&url=http%3A%2F%2Fscikit-surgery.org
   :target: https://twitter.com/intent/tweet?screen_name=scikit_surgery&ref_src=twsrc%5Etfw
   :alt: Get in touch via twitter

.. image:: https://img.shields.io/twitter/follow/scikit_surgery?style=social
   :target: https://twitter.com/scikit_surgery?ref_src=twsrc%5Etfw
   :alt: Follow scikit_surgery on twitter

This is a set of scripts to get statistics on the scikit-surgery library
and turn them into a nice webpage

.. image:: https://github.com/scikit-surgery/scikit-surgery-stats/raw/master/assets/screenshot.png
    :width: 400px
    :target: http://scikit-surgery.github.io/scikit-surgery-stats/
    :alt: Link to the dashboard



Use instructions
=================    

1. Activating the environment

        mkdir env

        python -m venv env/

        source env/bin/activate

        pip install -r requirements

2. Make sure you have a personal access token for Github API generated from `here <https://github.com/settings/personal-access-tokens/new>`_
    and is saved in the base directory under a file named `github.token`

3. Running the pipeline that generates dashboard.html and associated files needed by Github Pages

        bash Makefile


*  Inspect libraries with pypi

        ./pypi-simple-search scikit-surgery > scikit-surgery-onpypi.txt

        python get_github_repos.py > scikit-surgery-ongithub.txt                                                                    

    We can use pypinfo to get data for things on pypi


        pypinfo --auth snappy-downloads-3d3fb7e245fd.json
        pypinfo scikit-surgeryvtk country
        
