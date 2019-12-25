import tweepy
# Fill the X's with the credentials obtained by
# following the above mentioned procedure.


# Function to extract tweets
def get_tweets(username):
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler("yh9QaGCF16myX7hhEC92R72Gj", "l9tVilQDW1E7SwPhGhGuC9ZFO2a2R0l5XhOuAPZxWJdfnNGwYd")
    auth.set_access_token("1239007165-7VuDU9dGQJ8yrOMXSQm4QKerg1tTktKkcFXHIGz",
                          "PLh3aKqDeqQlaUyJHHqbjvayCqs0ths35Kjk9JN8B4wKw")
    # Calling api
    api = tweepy.API(auth)

    # 200 tweets to be extracted
    number_of_tweets = 200
    tweets = api.user_timeline(screen_name=username)

    # Empty Array
    tmp = []

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append(j)

    # Printing the tweets
    print(tmp)


# Driver code
if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.


    get_tweets("twitter-handle")
