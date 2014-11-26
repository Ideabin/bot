""" Idea related functions. """

import json
import users
import sqlite3
import datetime as dt
from collections import namedtuple

from urllib.parse import urlencode
from urllib.request import urlopen

import db

GISTS_URL = "https://api.github.com/users/{0}/gists?"

Idea = namedtuple('Idea', 'username, gistid, description, tweetid')


def add(user, gist):
    """ Create a new user. """

    idea = Idea(user.username, gist['id'], gist['description'], None)
    sql = "INSERT INTO ideas VALUES (?, ?, ?, ?);"
    try:
        db.write(db.con, sql, idea)
    except sqlite3.IntegrityError:
        pass



def fetch_gists(user):
    """ Fetch gists from github. """

    url = GISTS_URL.format(user.username)
    params = {
        'client_id': db.config["Github"]["Client_Id"],
        'client_secret': db.config["Github"]["Client_Secret"]
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
