class User:

	def __init__(self, id, name, description, created_at, followers, location):
		self.id = id
		self.name = name
		self.description = description
		self.created_at = created_at
		self.followers = followers
		self.location = location
		

	def __str__(self):
		return "User: {name}, Description: {description}, Followers: {followers}".format(name=self.name,
																						 description=self.description,
																						 followers=self.followers)
