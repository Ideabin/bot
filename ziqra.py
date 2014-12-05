""" Tweets out un-tweeted ideas. """

import ideas
import tweets

from db import config

LIMIT = int(config["Constants"]["Tweets_Per_Hour"]) / 2

for count, idea in enumerate(ideas.get_untweeted()):
    if count == LIMIT:
        break

    tweet = tweets.new(idea)
    ideas.set_tweetid(tweet.id)
