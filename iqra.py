""" Fetches idea gists and stores them to the database. """

import db
import users
import ideas

# Initialize the database
db.init()

# Add all registered users to db
for user in users.fetch_registered():
    users.add(user)

# Fetch gists of every user
for user in users.get_all():

    for gist in ideas.fetch_gists(user):

        if not gist['description']:
            continue

        # Extract gists that are ideas
        if "#ideabin" in gist['description']:
            ideas.add(user, gist)
