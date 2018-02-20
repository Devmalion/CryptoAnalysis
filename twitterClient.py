
import tweepy
from tweepy import OAuthHandler
import os
from os.path import join, dirname
from dotenv import find_dotenv, load_dotenv
from streamListener import StreamListener

# TwitterClient i
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
		stream_listener = StreamListener()
		stream = tweepy.Stream(auth=self.api.auth, listener=stream_listener)
		stream.filter(track=filters)

		
if __name__ == "__main__":
	twitter_client = TwitterClient()
	twitter_client.create_stream(['crypto', 'cryptocurrency', 'xrp', 'btc', 'bitcoin', 'ripple'])

