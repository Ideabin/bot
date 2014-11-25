""" User related functions. """

import sqlite3
from collections import namedtuple
from urllib.request import urlopen

import db

User = namedtuple('User', 'username, twitter, email, last_fetch')


def fetch_registered():
    """
    Fetch all registered users from the repository.

    Register yourself at: https://github.com/Ideabin/registration
    """

    REGISTERED_USERS_URL = "https://raw.githubusercontent.com/" \
        "Ideabin/registration/master/Users"

    users = []

    try:
        data = urlopen(REGISTERED_USERS_URL).read().decode('utf-8')
    except:
        print("URL exception occured.")
    else:
        for line in data.split('\n'):

            if not (line == '' or line.startswith('#')):

                user_data = line.split(',')

                try:
                    username = user_data[0].strip()
                except:
                    print("Github username is required.")
                    continue

                try:
                    twitter = user_data[1].strip()
                    twitter = twitter if twitter != '' else None
                except:
                    twitter = None

                try:
                    email = user_data[2].strip()
                    email = email if email != '' else None
                except:
                    email = None

                # Love me some tuples
                users.append(User(username, twitter, email, None))
    return users
