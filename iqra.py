""" Fetches idea gists and stores them to the database. """

import db
import users

# Initialize the database
db.init()

# Add all registered users to db
for user in users.fetch_registered():
    users.add(user)

# Fetch gists of every user
for user in users.all():
    print(user)
