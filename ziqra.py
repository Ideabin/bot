""" Tweets out un-tweeted ideas. """

import ideas
import tweets

from db import config

LIMIT = int(config.get("Constants","Tweets_Per_Hour")) / 2

# Only tweet LIMIT no. of untweeted ideas.
# So that we never break the Twitter tweet limits.
for count, idea in enumerate(ideas.get_untweeted()):
	if count == LIMIT:
		break

	tweet = tweets.new(idea)
	if tweet:
		ideas.set_tweetid(idea, tweet.id)
