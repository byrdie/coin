import string
from twitterscraper import query_tweets

query = 'from%3Aofficialmcafee'

tweet_lst = query_tweets(query,10)

# punctuation = set(string.punctuation)

for tweet in tweet_lst:
    txt = tweet.text
    if 'Coin of the day' in txt:

        coin= ''
        ind = []
        j = 0
        for i in range(len(txt)):

            if txt[i].isupper():

                if ind == []:
                    ind.append(i)
                    # print(i)
                    # print(txt[i])
                    j = j + 1
                elif ind[j - 1] == i - 1:
                    ind.append(i)
                    # print(i)
                    j = j + 1
            else:
                if j >= 2:
                    break
                else:
                    ind = []
                    j = 0

        for i in ind:
            coin = coin + txt[i]

        print(coin)