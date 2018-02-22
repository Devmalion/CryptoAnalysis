from TwitterClient import TwitterClient
from Analysis import Analysis

if __name__ == '__main__':
	twitter_client = TwitterClient()
	# twitter_client.create_stream(['crypto', 'cryptocurrency', 'xrp', 'btc', 'bitcoin', 'ripple'])
	# twitter_client.sample_tweets("python", 100)
	# twitter_client.backfill_tweets()
	analysis = Analysis()
	print(analysis.find_general_sentiment())
	analysis.generate_user_sentiment()