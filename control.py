#joblib
import joblib
#regex
import re
#translation
from google_trans_new import google_translator  
#transliteration
import aaransia
from aaransia import transliterate
from aaransia import SourceLanguageError
#Twitter
from tweepy import API 
from tweepy import OAuthHandler
#NumPy And Pandas
import numpy as np 
import pandas as pd 
# Naive bays
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
#My classes

from Myclasses import TwitterAuthenticator, TwitterClient, TweetAnalyzer





def predections_percent(predections):
	positive = 0
	negative = 0
	for predection in predections:
		if predection == '4':
			positive +=1
		else :
			negative +=1
        
	negative = negative * 100 /predections.shape[0]
	positive = positive * 100  /predections.shape[0]
	return(positive, negative)

def top_words(tweets_data):
	#getting most 20 repeated words
	vectorizer =  joblib.load("vectorizerNgram_1_2.sav")
	vectorizer_temp = CountVectorizer(stop_words= 'english')
	vectorizer_temp.fit(tweets_data['tweets'])
	val_temp=vectorizer_temp.transform(tweets_data['tweets'])

	#getting most 20 repeated words
	sum_words_temp = val_temp.sum(axis=0)
	val_temp.sum(axis=0)
	words_freq_temp = [(word, sum_words_temp[0, idx]) for word, idx in vectorizer_temp.vocabulary_.items()]
	words_freq_temp =sorted(words_freq_temp, key = lambda x: x[1], reverse=True)
	words = []
	frequencies = []
	for i in range(0,20):
		words.append( words_freq_temp[i][0])
		frequencies.append( words_freq_temp[i][1])
	return(words,frequencies)


def get_id(data):
	maxR = np.max(data['retweets'])
	id_M = 0
	indice = -1
	for i in data["retweets"]:
	    indice +=1
	    if i == maxR:
	        id_M = indice
	        break
	return data["id"][id_M]

	



def get_tweets(company):
	model =  joblib.load("My_Trained_Model_ar_Ngram_2_1.sav")
	vectorizer =  joblib.load("vectorizer.sav")
	# HERE we collect data from twitter based on a given word
	twitter_client = TwitterClient()
	tweet_analyzer = TweetAnalyzer()
	api = twitter_client.get_twitter_client_api()
	tweets = api.search(q=company, count = 50)
	tweets_data = tweet_analyzer.tweets_to_data_frame(tweets) 
	max_likes = np.max(tweets_data['likes'])
	max_retweets = np.max(tweets_data['retweets'])
	vect_tweets = vectorizer.transform(tweets_data['tweets'])
	predections = model.predict(vect_tweets)
	words, frequencies = top_words(tweets_data)
	pos , neg = predections_percent(predections)
	id_M = get_id(tweets_data)
	likes_T = [i for i in tweets_data['likes']];
	retweets_T = [i for i in tweets_data['retweets']];
	dates = [str(i) for i in  (tweets_data['dates'])];

	return(pos, neg, words, frequencies,likes_T,retweets_T, max_likes, max_retweets,dates,id_M)



	