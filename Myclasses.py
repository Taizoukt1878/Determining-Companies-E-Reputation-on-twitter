#regex
import re
#translation
#from google_trans_new import google_translator
from textblob import TextBlob  
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


#twitter Infos
Con_key = " You can get this parametere by creating a TwitterAPI Account"
Con_sec = " You can get this parametere by creating a TwitterAPI Account"
access_T= " You can get this parametere by creating a TwitterAPI Account"
access_S= " You can get this parametere by creating a TwitterAPI Account"

# this class helps us to authenticate twitter account
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(Con_key, Con_sec)
        auth.set_access_token(access_T, access_S)
        return auth

#  this class connects us to the api 
class TwitterClient():
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

    def get_twitter_client_api(self):
        return self.twitter_client


# this class handels the tweets (cleaning and filtring needed data)
class TweetAnalyzer():
    def remove_rep(self, r):
        r = re.sub(r'(a){3,10}',r'\1',r)
        r = re.sub(r'(b){3,10}',r'\1',r)
        r = re.sub(r'(c){3,10}',r'\1',r)
        r = re.sub(r'(d){3,10}',r'\1',r)
        r = re.sub(r'(e){3,10}',r'\1',r)
        r = re.sub(r'(f){3,10}',r'\1',r)
        r = re.sub(r'(i){3,10}',r'\1',r)
        r = re.sub(r'(j){3,10}',r'\1',r)
        r = re.sub(r'(k){3,10}',r'\1',r)
        r = re.sub(r'(l){3,10}',r'\1',r)
        r = re.sub(r'(m){3,10}',r'\1',r)
        r = re.sub(r'(n){3,10}',r'\1',r)
        r = re.sub(r'(o){3,10}',r'\1',r)
        r = re.sub(r'(p){3,10}',r'\1',r)
        r = re.sub(r'(q){3,10}',r'\1',r)
        r = re.sub(r'(r){3,10}',r'\1',r)
        r = re.sub(r'(s){3,10}',r'\1',r)
        r = re.sub(r'(t){3,10}',r'\1',r)
        r = re.sub(r'(u){3,10}',r'\1',r)
        r = re.sub(r'(v){3,10}',r'\1',r)
        r = re.sub(r'(w){3,10}',r'\1',r)
        r = re.sub(r'(x){3,10}',r'\1',r)
        r = re.sub(r'(y){3,10}',r'\1',r)
        r = re.sub(r'(z){3,10}',r'\1',r)
#Maj
        r = re.sub(r'(A){3,10}',r'\1',r)
        r = re.sub(r'(B){3,10}',r'\1',r)
        r = re.sub(r'(C){3,10}',r'\1',r)
        r = re.sub(r'(D){3,10}',r'\1',r)
        r = re.sub(r'(E){3,10}',r'\1',r)
        r = re.sub(r'(F){3,10}',r'\1',r)
        r = re.sub(r'(I){3,10}',r'\1',r)
        r = re.sub(r'(J){3,10}',r'\1',r)
        r = re.sub(r'(K){3,10}',r'\1',r)
        r = re.sub(r'(L){3,10}',r'\1',r)
        r = re.sub(r'(M){3,10}',r'\1',r)
        r = re.sub(r'(N){3,10}',r'\1',r)
        r = re.sub(r'(O){3,10}',r'\1',r)
        r = re.sub(r'(P){3,10}',r'\1',r)
        r = re.sub(r'(Q){3,10}',r'\1',r)
        r = re.sub(r'(R){3,10}',r'\1',r)
        r = re.sub(r'(S){3,10}',r'\1',r)
        r = re.sub(r'(T){3,10}',r'\1',r)
        r = re.sub(r'(U){3,10}',r'\1',r)
        r = re.sub(r'(V){3,10}',r'\1',r)
        r = re.sub(r'(V){3,10}',r'\1',r)
        r = re.sub(r'(X){3,10}',r'\1',r)
        r = re.sub(r'(Y){3,10}',r'\1',r)
        r = re.sub(r'(Z){3,10}',r'\1',r) 
        return r
    
    def clean_tweet(self, tweet):
        word = ""
        tweet_temp = ""
        tweet = self.remove_rep(tweet)
        #My_Trans = google_translator ()
        tweet_B = TextBlob(tweet)

        if (tweet_B.detect_language() != 'en'):
            if(tweet_B.detect_language() == 'ar'):
                for lettre in tweet:
                    if (lettre != " "):
                        try:
                            word = word + transliterate(lettre, source='ar', target='ma')
                        except:
                            word = word + lettre
                    else:
                        word = word + " "
                        tweet_temp = tweet_temp + word
                        word = ""
                tweet = tweet_temp
            else:
                try:
                 tweet = tweet_B.translate(to = 'en')
                 tweet = str(tweet)
                except:
                    tweet = " "

                     
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|(\w+:\/\/\S+)|(#[A-Za-z0-9]+| [0-9]+)", " ", tweet).split())
    
    def tweets_to_data_frame(self, tweets):
        df= pd.DataFrame(data=[self.clean_tweet(tweet.text) for tweet in tweets], columns=['tweets'])
        df['dates'] = np.array([tweet.created_at for tweet in tweets])
        df['id'] = np.array([tweet.id_str for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        return df