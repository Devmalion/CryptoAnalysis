import TextBlob

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



	def __str__(self):
		return "Text: {text}, Retweets: {retweets}, Favorites: {favorites}".format(text=self.text,
																				   retweets=self.retweets,
																				   favorites=self.favorites)



