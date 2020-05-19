colinpollock.net
================

## Setup ##
1. `$ python3.7 -m venv .venv`
2. `$ source .venv/bin/activate`
3. `$ pip install --upgrade pip`
4. `$ pip install -r requirements.txt`
5. `$ git clone git@github.com:colinpollock/brutalist.git`
6. `$ pelican-themes --install brutalist`. Use `--upgrade` instead of the theme was previously installed.
7. `$ make devserver`
8. Go to http://localhost:8000/

## To update GH Pages ##
1. `make github`
