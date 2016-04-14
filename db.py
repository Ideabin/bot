""" Provide database interactions to the bots. """

import os
import sqlite3
from configparser import ConfigParser

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

config = ConfigParser()
config.read(os.path.join(CURRENT_DIR, 'config.ini'))

DATABASE = config["Database"]["File"]

# Detect no types. We'll parse everything on our own.
# Done because reading Idea.created_at was causing problems.
con = sqlite3.connect(DATABASE, detect_types=0)


def init():
    """ Initialize the databse. """

    with con:
        create_tables(con)


def write(con, sql, values):
    """ Execute an Insert SQL Query. """

    with con:
        con.cursor().execute(sql, values)
        con.commit()


def read(con, sql, values=None):
    """ Perform read operations on the databse. """

    result = None
    with con:
        if values:
            cur = con.cursor().execute(sql, values)
        else:
            cur = con.cursor().execute(sql)

        result = cur.fetchall()

    return result


def create_tables(con):
    """ Create tables. """

    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            username    VARCHAR( 200 )      PRIMARY KEY
                                            NOT NULL,

            twitter     VARCHAR( 200 )      UNIQUE,

            email       VARCHAR( 200 )      UNIQUE,

            last_fetch  TIMESTAMP
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ideas (
            gistid      VARCHAR( 20 )   PRIMARY KEY
                                        NOT NULL,

            username    VARCHAR( 200 )  NOT NULL,

            description VARCHAR( 500 ),

            created_at  TIMESTAMP,

            tweetid     INT( 20 )       UNIQUE,

            FOREIGN KEY ( username )    REFERENCES users ( username )
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS id_value (
            tweet_id    INT ( 20 )   PRIMARY KEY
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS retweets (
            retweet_id   INT( 20 )   UNIQUE,
            retweeted_at    TIMESTAMP   PRIMARY KEY
        );
        """
    )

    con.commit()
