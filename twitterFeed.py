from TwitterClient import TwitterClient

if __name__ == '__main__':
	twitter_client = TwitterClient()
	twitter_client.create_stream(['crypto', 'cryptocurrency', 'xrp', 'btc', 'bitcoin', 'ripple'])
