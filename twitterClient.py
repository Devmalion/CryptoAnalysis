import tweepy
import os
from tweepy import OAuthHandler
from os.path import join, dirname
from dotenv import find_dotenv, load_dotenv
from StreamListener import StreamListener

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

		# Attempt Connection to Twitter API
		try:
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token, access_secret)
			self.api = tweepy.API(self.auth)
		except:
			print("Connection To Twitter Failed")


	def create_stream(self, filters=[]):
		db_file = os.environ["db_file"]
		stream_listener = StreamListener(db_file)
		stream = tweepy.Stream(auth=self.api.auth, listener=stream_listener)
		stream.filter(track=filters)


	def sample_tweets(self, query):
		



