""" Provide database interactions to the bots. """

import os
import sqlite3
from configparser import ConfigParser

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

config = ConfigParser()
config.read(os.path.join(CURRENT_DIR, 'config.ini'))

DATABASE = config["Database"]["File"]

con = sqlite3.connect(DATABASE)


def init():
    """ Initialize the databse. """

    with con:
        create_tables(con)


def write(con, sql, values):
    """ Execute an Insert SQL Query. """

    with con:
        con.cursor().execute(sql, values)
        con.commit()


def read(con, sql):
    """ Perform read operations on the databse. """

    result = None
    with con:
        cur = con.cursor()
        cur.execute(sql)
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

            last_fetch  DATETIME
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ideas (
            username     VARCHAR( 200 )     PRIMARY KEY
                                            NOT NULL,

            gistid       VARCHAR( 20 )      NOT NULL
                                            UNIQUE,

            description VARCHAR( 500 ),

            FOREIGN KEY(username) REFERENCES users(username)
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tweets (
            username     VARCHAR( 200 )     PRIMARY KEY
                                            NOT NULL,

            tweetid      VARCHAR( 20 )      NOT NULL
                                            UNIQUE,

            message      VARCHAR( 140 ),

            FOREIGN KEY(username) REFERENCES users(username)
        );
        """
    )

    con.commit()
