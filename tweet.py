import tweepy
import pandas as pd

api_key = 'mULVUvRdjCIPIey6NHpzEd1zr'
access_token_secret = 'Df49VRn803KJsmzTCo1geL0AJBkkKemxM7Hjm1SQAiqxL'

auth = tweepy.OAuthHandler(api_key, 'wYU9Ps3EpnDz9rqZPqu51Cyiyyg3l7sPBGp9ulsNulEikrdun2')
auth.set_access_token('1524269999375986688-cJdMOVAPkX9yrOihh3zI3g4MbTCea1', access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
# print(public_tweets) # print all homepage tweets
# print(public_tweets[0].text) # print first tweet only
# print(public_tweets[0].created_at) # print timing of tweets
# print(public_tweets[0].user.name) # print username

data = []
col = ['Time', 'User', 'Tweet']
for tweet in public_tweets:
 print(tweet.text) # print all tweets
 print(tweet.created_at) # print timing for tweets
 print(tweet.user.name) # print user name
 data.append([tweet.created_at, tweet.user.name, tweet.text])
print(data)
df = pd.DataFrame(data, columns=col)
# print(df)
df.to_csv('tweets.csv', index=False)