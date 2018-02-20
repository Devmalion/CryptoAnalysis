import tweepy

# StreamListener is a subclass of the main StreamListener from the Tweepy API
# We create the subclass to override logic for handling tweets 
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
    	if hasattr(status, 'retweeted_status'):
    		return
    	print(status.text)

        
    def on_error(self, status_code):
        if status_code == 420:
            return False