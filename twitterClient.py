import tweepy
import os
import sqlite3
from tweepy import OAuthHandler
from os.path import join, dirname
from dotenv import find_dotenv, load_dotenv
from StreamListener import StreamListener
from User import User
from Tweet import Tweet

# TwitterClient handles the connection to the Twitter API using Tweepy and processes the streaming API
class TwitterClient:

	def __init__(self):

		# Load Environment Variables
		envPath = join(dirname(__file__), '.env')
		load_dotenv(envPath)

		# Initialize API keys
		consumer_key = os.environ["consumer_key"]
		consumer_secret = os.environ["consumer_secret"]
		access_token = os.environ["access_token"]
		access_secret = os.environ["access_secret"]

		self.db_file = os.environ["db_file"]

		# Attempt Connection to Twitter API
		try:
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token, access_secret)
			self.api = tweepy.API(self.auth)
		except:
			print("Connection To Twitter Failed")


	def create_stream(self, filters=[]):
		stream_listener = StreamListener(self.db_file)
		stream = tweepy.Stream(auth=self.api.auth, listener=stream_listener)
		stream.filter(track=filters)


	def sample_tweets(self, query, amount):
		tweets = []
		for tweet in tweepy.Cursor(self.api.search,
								   q=query,
								   lang="en").items(amount):
			tweets.append(tweet)
		
		return tweets

	def find_tweet(self, tweet_id):
		return self.api.statuses_lookup([tweet_id])


	# Note the Twitter API only allows a max of 100 tweets to be looked up at a time
	def find_tweets(self, tweet_ids):
		return self.api.statuses_lookup(tweet_ids)


	def backfill_tweets(self):
		conn = sqlite3.connect(self.db_file)
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM tweets")
		rows = cursor.fetchall()

		STATUS_ID = 1
		count = 0
		search = []
		updateDict = {}
		for row in rows:
			search.append(row[STATUS_ID])
			count += 1

			if count == 100:
				self.update_tweets(self.find_tweets(search), conn)
				search = []
				count = 0

		self.update_tweets(self.find_tweets(search), conn)


	def update_tweets(self, tweets, conn):
		cursor = conn.cursor()
		for status in tweets:
			cursor.execute("""UPDATE tweets SET 
							  favorites = {favorite_count},
							  retweets = {retweet_count}
							  WHERE id = {status_id}""".format(favorite_count=status.favorite_count,
							  								   retweet_count=status.retweet_count,
							  								   status_id=status.id))
			conn.commit()
			








	




