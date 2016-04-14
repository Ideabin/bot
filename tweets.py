""" Tweets out an idea's descriptions. """

import users
from db import config
from collections import namedtuple
from twython import Twython

twitter = Twython(
	config["Twitter"]["Consumer_Key"],
	config["Twitter"]["Consumer_Secret"],
	config["Twitter"]["Access_Token_Key"],
	config["Twitter"]["Access_Token_Secret"]
)

GIST_URL = "https://gist.github.com/{0}"

Tweet = namedtuple('Tweet', 'id, msg')


def new(idea):
	""" Post a new tweet. """

	user = users.from_name(idea.username)
	if user.twitter:
		msg = ".@" + user.twitter + " - "
	else:
		msg = "New idea: "

	msg = tweetify(msg, idea.description, GIST_URL.format(idea.gistid))
	tweet = twitter.update_status(status=msg)
	return Tweet(tweet['id'], msg)


def tweetify(msg, desc, link):
	""" Return a nice tweetable message . """

	# 22 characters are for shortening of link to 't.co'
	# Additional 1 is for ' '

	if len(msg + desc) <= 140 - 22 - 1:
		return msg + desc + ' ' + link
	else:
		return msg + link

def tweetout(status, last_tweet_id):
	twitter.update_status(status=status, in_reply_to_status_id=last_tweet_id)
