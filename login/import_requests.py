import tweepy
from tweepy import OAuthHandler

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



#Variables that contains the user credentials to access Twitter API 
access_token = '4788049051-CLAnbSEnbBa3t351CPPDgkXO9kma1D01uC9tTyl'
access_secret = 'jVNj9JS4Bljs6f5GvLvSlzlxLKLyYEekLhAUq8C5fkjkD'
consumer_key = '5buqizE9pwVxQNDWzqWf9bnLQ'
consumer_secret = '5cGJeFLlDf6NtQEEdDegQ43iRPK8LqRUOQctRdOvmEw1zwVt9t'

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])