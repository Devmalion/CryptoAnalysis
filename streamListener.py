import tweepy
import sqlite3
from Tweet import Tweet
from User import User

# StreamListener is a subclass of the main StreamListener from the Tweepy API
# We create the subclass to override logic for processing tweets 
class StreamListener(tweepy.StreamListener):

	def __init__(self, db_file):
		super(StreamListener, self).__init__()
		self.conn = sqlite3.connect(db_file)

	# Method override that processes each incoming tweet
	def on_status(self, status):
		if hasattr(status, 'retweeted_status'):
			return

		cursor = self.conn.cursor()
		# User Fields
		user_id = status.user.id
		name = status.user.screen_name
		description = status.user.description
		user_created = status.user.created_at
		followers = status.user.followers_count
		loc = status.user.location

		statusUser = User(user_id, name, description, user_created, followers, loc)

		# Tweet Fields
		id = status.id
		text = status.text
		created = status.created_at
		retweets = status.retweet_count
		favorites = status.favorite_count
		coords = status.coordinates

		status = Tweet(statusUser, id, text, created, retweets, favorites, coords)

		print(statusUser)
		print(status)

		try:
			cursor.execute('''INSERT INTO users(user_id, name, description, user_created, followers, loc)
							  VALUES(?, ?, ?, ?, ?, ?)''', (user_id, name, description, user_created, followers, loc))
		except:
			print("User already in DB")
		try:
			cursor.execute('''INSERT INTO tweets(user_id, id, text, created_at, retweets, favorites, coords)
							  VALUES(?, ?, ?, ?, ?, ?, ?)''', (user_id, id, text, created, retweets, favorites, coords))
		except:
			print("Tweet could not be added to DB")
			
		self.conn.commit()


		def on_error(self, status_code):
			if status_code == 420:
				return False


		def __del__(self):
			self.conn.close()
			super(StreamListener, self).__del__()