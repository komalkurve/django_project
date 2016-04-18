import tweepy
from tweepy import OAuthHandler
import time
import re
import json
import pandas as pd
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from models import Twit,Twittime,Twitlocation
from datetime import datetime




#Variables that contains the user credentials to access Twitter API 


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self,time_limit):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('requests.json','a')
        super(StdOutListener,self).__init__()

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            self.saveFile.write(data)
            self.saveFile.write('\n')
            return True
        else:
            self.saveFile.close()
            return False

    def on_error(self, status):
        print(status)




class Tweet_data(object):
    def __init__(self,keyword,freq,keyword_num):
        self.keyword = keyword
        self.freq = freq
        self.keyword_num = keyword_num
        



class Tweet_final(object):
    def __init__(self):
        self.access_token = '4788049051-CLAnbSEnbBa3t351CPPDgkXO9kma1D01uC9tTyl'
        self.access_secret = 'jVNj9JS4Bljs6f5GvLvSlzlxLKLyYEekLhAUq8C5fkjkD'
        self.consumer_key = '5buqizE9pwVxQNDWzqWf9bnLQ'
        self.consumer_secret = '5cGJeFLlDf6NtQEEdDegQ43iRPK8LqRUOQctRdOvmEw1zwVt9t'
        self.tweets = pd.DataFrame()    

    
    def getwords(self,string):
        return re.findall(r"[\w'#]+|[.,!?;]",string)

    def freq_count(self,keyword):
        return(self.tweets[keyword].value_counts()[True])

    def word_in_text(self,word, text):
       word = word.lower()
       text = text.lower()
       match = re.search(word, text)
       if match:
          return True
       return False

    def cal_time(self):
     #This handles Twitter authetification and the connection to Twitter Streaming API
     auth = OAuthHandler(self.consumer_key, self.consumer_secret)
     auth.set_access_token(self.access_token, self.access_secret)

     time_limit = input("Enter the time limit in minutes : ")
     time_limit *= 60


     stream = Stream(auth,listener = StdOutListener(time_limit))
     string = raw_input("Enter the keywords/hashtags : ")

     keyword_list = self.getwords(string)


     #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
     stream.filter(track = keyword_list)
     
     tweets_data_path = 'requests.json'
     tweets_file = open(tweets_data_path, "r")
     tweets_data = []
     for line in tweets_file:
        try:
            tweet = json.loads(line)
            
        except:
            continue

        if not all(x in tweet for x in ['text','lang','place']):
            continue
        if tweet['place'] and not 'country' in tweet['place']:
            continue
        tweets_data.append(tweet)


    
     self.tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
     self.tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
     self.tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
     self.tweets['coordinates'] = map(lambda tweet: tweet['coordinates'],tweets_data)



     tweets_by_lang = self.tweets['lang'].value_counts()
     tweets_prog_lang = self.tweets['text'].value_counts()
     tweets_by_country = self.tweets['country'].value_counts()

   

     for keyword in keyword_list:
        self.tweets[keyword] = self.tweets['text'].apply(lambda tweet: self.word_in_text(keyword, tweet))
        
    


     key_num = 0
     tweet_object = []
     frequency = []

     for keyword in keyword_list:
        freq = self.freq_count(keyword)
        tweet_object.append(Tweet_data(keyword,freq,key_num)) 
        frequency.append(freq)
        key_num += 1

     for i in tweet_object:
         p = Twittime(keyword = i.keyword, freq = i.freq, time=datetime.now())
        
         p.save()


