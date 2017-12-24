from twitterscraper import query_tweets

query = 'from%3Aofficialmcafee'

tweet_lst = query_tweets(query,10)

for tweet in tweet_lst:
    txt = tweet.text
    if 'Coin of the day' in txt:
        print(txt)
        print()

