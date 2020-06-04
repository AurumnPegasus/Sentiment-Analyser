import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('coronavirus').setSince("2019-11-11").setMaxTweets(2000).setNear("Kolkata, India")
f = open('data.txt','a+')

tweets = got.manager.TweetManager.getTweets(tweetCriteria)
print("got tweets")
for tweet in tweets:
    f.write(tweet.text)
    f.write("\n")
