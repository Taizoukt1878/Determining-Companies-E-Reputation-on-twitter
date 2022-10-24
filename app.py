from flask import Flask,render_template,request, url_for,make_response,session
from models import *
from charts import make_charts
from control import get_tweets
import pdfkit

# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta,date
#import os

#from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'azertyui'
#CORS(app)
#the route is the page where data will be sent  
@app.route('/', methods = ['GET', 'POST'])

def index():
	result = -1
	message = ""
	words = []
	frequincies = []
	pos = -1
	if request.method == 'GET':
		pass
	if request.method == 'POST':
		name = request.form.get('username')
		session['name'] = name
		password = request.form.get('password')
		result = login(name,password)
	if (result == 1):
		session["userId"] = get_userId(name,password) 
		result = get_companies()
		return render_template('home_search.html' , name = name,result = result )
	elif( result == 0):
		return render_template('index.html' , message = "username or password is wrong")
	else:
		return render_template('index.html')


#######################
@app.route('/login_man', methods = ['GET', 'POST'])

def index_man():
	result = -1
	message = ""
	pos = -1
	if request.method == 'GET':
		pass
	if request.method == 'POST':
		name = request.form.get('username')
		session['name'] = name
		password = request.form.get('password')
		result = login_man(name,password)
	if (result == 1):
		#Mise_a_jour()
		companies = get_proposed()
		return render_template('proposed.html' , name = name, result = companies )
	elif( result == 0):
		return render_template('index_man.html' , message = "username or password is wrong")
	else:
		return render_template('index_man.html')


#########################
@app.route('/manager', methods = ['GET', 'POST'])

#Login Manager

def home_manager():
	result = -1
	pos = -1
	if request.method == 'GET':
		pass
	if request.method == 'POST':
		ename = request.form.get('proposed')
		ename = ename.lower()
		result = add_ename(ename)
		return render_template('proposed.html' ,name = session['name'], result = result )
	else:
		result = get_proposed()
		return render_template('proposed.html',name = session['name'], result = result )


@app.route('/register', methods = ['GET', 'POST'])

def register():
	result = -1
	if request.method == 'POST':
		name = request.form.get('username')
		password = request.form.get('password')
		conf_password = request.form.get('conf_password')
		result = sign_up(name, password,conf_password)
	if (result == 0):
			return render_template('register.html' , result=result)
	elif(result == 1):
			return render_template('index.html' , result = result)
	else:
			return render_template('register.html' , result = result)



@app.route('/home', methods = ['GET', 'POST'])
def home():
	result = -1
	message = ""
	words = []
	frequincies = []
	likes_T = []
	retweets_T = []

	if request.method == 'POST':
		company = request.form.get('ename')
		company = company.lower()
		session['comp'] = company
		result = company_check(company)
		if (result == 0):
			pos = -1
			return render_template('home_search.html',name = session['name'], message ="can't find this name on our companies database", pos = pos)
		elif(result == 1):
			test_exist = test_data(company)
			if (test_exist == 1):
				pos, neg, words, frequincies,likes_T,retweets_T, max_L,max_R,dates,id_M = get_data(company)
				return render_template('search.html',name = session['name'],company = company, pos = pos, neg = neg, words = words, frequincies= frequincies, max_L = max_L,max_R= max_R, likes_T = likes_T, retweets_T = retweets_T, dates = dates, id_M = id_M )

				
			else:
				pos, neg, words, frequincies,likes_T,retweets_T, max_L,max_R,dates,id_M = get_tweets(company)
				S_words = ", ".join(words)
				S_frequincies = ", ".join(map(str, frequincies))
				S_likes_T = ", ".join(map(str, likes_T))
				S_retweets_T = ", ".join(map(str, retweets_T))
				S_dates = ", ".join(map(str, dates))
				insert_data(company, float(pos), float(neg), S_words, S_frequincies, S_likes_T, S_retweets_T, int(max_L), int(max_R), S_dates,id_M)
				return render_template('search.html',name = session['name'], pos = pos, neg = neg, words = words, frequincies= frequincies, max_L = max_L,max_R= max_R, likes_T = likes_T, retweets_T = retweets_T, dates = dates, id_M = id_M )
			
	else:
		pos = -1
		result = get_companies()
		return render_template('home_search.html' ,name = session['name'], message = message, result = result)

#/////////////////////

@app.route('/home/pdf', methods = ['GET', 'POST'])

def pdf_generator():
	#pos, neg, words, frequincies,likes_T,retweets_T, max_L,max_R,dates,id_M = get_data(session['comp'])
	WIDTH = 210
	HEIGHT = 297
	company = session['comp']
	make_charts(company)
	day = date.today().strftime("%Y-%m-%d")
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font('Arial', 'BI', 26)
	pdf.set_fill_color(47, 179, 255)
	pdf.cell(176,20,'T-E-Rep',1,0,'C',fill = True)
	pdf.ln(1)
	pdf.set_font('Arial', 'I', 14) 
	pdf.cell(176,50,f'Edited at :{day}',0,0,'C')
	pdf.ln(50)
	pdf.set_font('Arial', 'BUI', 18)
	pdf.set_text_color(47, 179, 255)
	pdf.write(5, f"{company.capitalize()} Twitter sentiment Analysis Report")
	pdf.ln(10)
	pdf.set_font('Arial', 'B', 16)
	pdf.set_text_color(7, 201, 201)
	pdf.write(4, 'I- Likes & Tweets')
	pdf.image("likes_and_tweets.jpg", 5, 83, WIDTH-20)
	pdf.ln(3)
	pdf.set_y(pdf.get_y()+63)
	pdf.write(4, 'II- Positive And negative tweets')
	pdf.image("Pie.jpg",5, 142, WIDTH-30, 80)
	pdf.ln()
	pdf.set_y(pdf.get_y()+72)
	pdf.write(4, 'III- Most repeated words')
	pdf.image("WordC.jpg",  5, 218, WIDTH-20,90)
	response = make_response(pdf.output(dest='S').encode('latin-1'))
	response.headers['content-type'] = 'application/pdf'
	response.headers['content-Disposition'] = 'attachment; filename = output.pdf'
	return response




@app.route('/propose', methods = ['GET', 'POST'])

def proposer():
	if request.method == 'POST':
		ep_name = request.form.get('epname')
		insert_epname(ep_name,session["userId"])
		return render_template('home_propose.html',name = session['name'])
	else:
		return render_template('home_propose.html',name = session['name'])

@app.route('/users', methods = ['GET', 'POST'])

def users():
	result = -1
	pos = -1
	if request.method == 'GET':
		pass
	if request.method == 'POST':
		ename = request.form.get('username')
		delete_user(ename)
		result = get_users()
		return render_template('users.html' ,name = session['name'], result = result )
	else:
		result = get_users()
		return render_template('users.html',name = session['name'], result = result )

@app.route('/companies', methods = ['GET', 'POST'])

def My_companies():
	result = -1
	pos = -1
	if request.method == 'GET':
		pass
	if request.method == 'POST':
		ename = request.form.get('company')
		delete_company(ename)
		result = get_companies()
		return render_template('companies.html' ,name = session['name'], result = result )
	else:
		result = get_companies()
		return render_template('companies.html',name = session['name'], result = result )





if __name__ == '__main__':
	app.run(debug = True)