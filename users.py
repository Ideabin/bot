""" User related functions. """

import sqlite3
import datetime as dt
from collections import namedtuple
from urllib.request import urlopen

import db

User = namedtuple('User', 'username, twitter, email, last_fetch')


def add(user):
	""" Create a new user. """

	sql = "INSERT INTO users VALUES (?, ?, ?, ?);"
	try:
		db.write(db.con, sql, user)
	except sqlite3.IntegrityError:
		# Do nothing when the record already exists
		pass


def get_all():
	""" Return all users present in the database. """

	fetchall = db.read(db.con, "SELECT * FROM users;")
	return map(User._make, fetchall)


def from_name(username):
	""" Return a user with the passed username. """

	sql = "SELECT * FROM users WHERE username = (?);"
	row = db.read(db.con, sql, (username,))
	return User._make(row[0])


def update_last_fetch(user):
	""" Set the last_fetch time of the user to the current time. """

	sql = "UPDATE users SET last_fetch = (?) WHERE username = (?);"
	db.write(db.con, sql, (dt.datetime.now(), user.username))


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
