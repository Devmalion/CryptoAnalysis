from textblob import TextBlob

class Tweet:

	def __init__(self, user, id, text, created, retweets, favorites, coords):
		self.user = user
		self.id = id
		self.text = text
		self.created = created
		self.retweets = retweets
		self.favorites = favorites
		self.coords = coords


	def analyze_sentiment(self):
		blob = TextBlob(self.text)
		self.sentiment = blob.sentiment
		return sentiment


	def __str__(self):
		return "Text: {text}, Retweets: {retweets}, Favorites: {favorites}".format(text=self.text,
																				   retweets=self.retweets,
																				   favorites=self.favorites)



