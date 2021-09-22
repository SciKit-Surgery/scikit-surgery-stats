scikit-surgery-stats
====================

.. raw:: html

    <a href="https://twitter.com/intent/tweet?screen_name=scikit_surgery&ref_src=twsrc%5Etfw" class="twitter-mention-button" data-show-count="false">Tweet to @scikit_surgery</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    <a href="https://twitter.com/scikit_surgery?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-show-count="false">Follow @scikit_surgery</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

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
