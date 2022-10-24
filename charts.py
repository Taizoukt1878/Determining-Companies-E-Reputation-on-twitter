import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from wordcloud import WordCloud
import numpy as np
import pandas as pd

def get_Tabels(company):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("SELECT * FROM company_data WHERE company = (%s)",(company,))
	data = my_curs.fetchall()
	#Ename = data[0][0]
	pos = data[0][1]
	neg = data[0][2]
	words = data[0][3].split(',')
	S_words = " ".join(words)
	likes_T = data[0][5].split(',')
	retweets_T = data[0][6].split(',')
	max_L = data[0][7]
	max_R = data [0][8]
	dates = data[0][9].split(',')
	return( pos, neg, S_words, likes_T, retweets_T, dates)

def make_charts(company):
	pos, neg, S_words, likes_T, retweets_T, dates = get_Tabels(company)
	likes = [int(i) for i in likes_T]
	retweets = [int(i) for i in retweets_T]
	figure(figsize=(12, 4), dpi=80)
	#Likes And tweets chart
	time_likes = pd.Series(data=likes, index=dates)
	time_likes.plot(figsize=(16, 4), color='r',label = 'likes',legend = True)
	time_likes = pd.Series(data=retweets, index=dates)
	time_likes.plot(figsize=(16, 4), color='g',label = 'retweets',legend = True)
	plt.savefig('likes_and_tweets.jpg')
	plt.close()
	# Pie chart Positive and negative tweets
	y = np.array([float(neg), float(pos)])
	mylabels = ["negative","Positive"]
	mycolors = ["red", "lightgreen"]
	#explode = (0.05, 0.05)
	plt.pie(y, labels = mylabels, colors = mycolors,autopct='%1.1f%%', pctdistance=0.85)
# draw circle
	centre_circle = plt.Circle((0, 0), 0.70, fc='white')
	fig = plt.gcf()
	  
	# Adding Circle in Pie chart
	fig.gca().add_artist(centre_circle)
	plt.savefig('Pie.jpg')
	plt.close()
	#wordCloud
	text_string = "".join(S_words)
	print(text_string)
	word = WordCloud(background_color="ghostwhite").generate(text_string)
	#plt.figure( figsize=(10,5), facecolor='k')
	plt.imshow(word)
	plt.axis("off")
	plt.tight_layout(pad=0)
	plt.savefig('WordC.jpg')
	plt.close()





