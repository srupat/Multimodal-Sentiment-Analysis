#referncing library with a shorter name,i.e got
# import GetOldTweets3 as got

# def get_tweets():
#   tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus')\
#                                            .setSince("2019-05-01")\
#                                            .setUntil("2021-09-30")\
#                                            .setMaxTweets(10)
#   tweets = got.manager.TweetManager.getTweets(tweetCriteria)
#   text_tweets = [[tweet.text] for tweet in tweets]
#   print(text_tweets)

# get_tweets()
import tweepy

def get_tweets(query, count):
    # Authenticate with Twitter API
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Fetch tweets
    tweets = []
    fetched_tweets = api.search_tweets(q=query, count=count)
    for tweet in fetched_tweets:
        tweets.append(tweet.text)
    
    return tweets

tweets = get_tweets('Python programming', 10)
print(tweets)

