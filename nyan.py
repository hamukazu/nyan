
import tweepy
import time
import mykey

auth = tweepy.OAuthHandler(mykey.consumer_key, mykey.consumer_secret)
auth.set_access_token(mykey.access_token, mykey.access_token_secret)

api = tweepy.API(auth)

for i in range(1, 11):
    api.update_status("にゃーん" * i)
    time.sleep(2)
