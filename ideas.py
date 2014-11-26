""" Idea related functions. """

import json
import users
import datetime as dt

from urllib.parse import urlencode
from urllib.request import urlopen

from db import config

GISTS_URL = "https://api.github.com/users/{0}/gists?"


def fetch_gists(user):
    """ Fetch gists from github. """

    url = GISTS_URL.format(user.username)
    params = {
        'client_id': config["Github"]["Client_Id"],
        'client_secret': config["Github"]["Client_Secret"]
    }

    if user.last_fetch:
        params['since'] = dt.datetime.isoformat(user.last_fetch)

    try:
        data = urlopen(url+urlencode(params)).read().decode('utf-8')
    except:
        data = []
    else:
        users.update_last_fetch(user)

    return json.loads(data)
