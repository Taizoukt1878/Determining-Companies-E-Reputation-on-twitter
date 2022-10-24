import mysql.connector
from datetime import date
from datetime import datetime

#//////////////////////////////////////// LOGIN

def login(name,passwd):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("SELECT COUNT(*) FROM User WHERE username = %s AND password = %s ",(name,passwd) )
	i= my_curs.fetchmany(size = 1)
	if (i[0][0] == 0):
		my_curs.close()
		db.close()
		return(0)
	else:
		my_curs.close()
		db.close()
		return(1)
#//////////////////////////////////////// LOGIN MANAGER

def login_man(name,passwd):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("SELECT COUNT(*) FROM gerant WHERE manager_name = %s AND password = %s ",(name,passwd) )
	i= my_curs.fetchmany(size = 1)
	if (i[0][0] == 0):
		my_curs.close()
		db.close()
		return(0)
	else:
		my_curs.close()
		db.close()
		return(1)

#//////////////////////////////////////// SIGN UP

def sign_up(name, passwd, conf_pass):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	if(passwd != conf_pass):
		my_curs.close()
		db.close()
		return(0)
	else:
		my_curs.execute("INSERT INTO User (username, password) VALUES (%s,%s)",(name, passwd))
		db.commit()
		my_curs.close()
		db.close()
		return(1)

#//////////////////////////////////////// COMPANY CHEK
def company_check(company):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("SELECT COUNT(*) FROM Entreprise WHERE Ename = %s",(company,) )
	i= my_curs.fetchmany(size = 1)
	if (i[0][0] == 0):
		my_curs.close()
		db.close()
		return(0)
	else:
		my_curs.close()
		db.close()
		return(1)


#//////////////////////////////////////// ADD ENAME

def add_ename(company):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	try:
		my_curs.execute("INSERT INTO Entreprise (ename) VALUES (%s)",(company,))
	except:
		pass
	my_curs.execute("DELETE FROM proposer WHERE EPname = (%s) " , (company,))
	db.commit()
	my_curs.execute("SELECT * FROM proposer")
	result = my_curs.fetchall()	
	my_curs.close()
	db.close()
	return result
#//////////////////////////////////////// GET PROPOSED COMPANIES

def get_proposed():
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("SELECT * FROM proposer")
	result = my_curs.fetchall()
	my_curs.close()
	db.close()
	return result
#//////////////////////////////////////// Propose ENAME

def insert_epname(company, userId):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	try:
		my_curs.execute("INSERT INTO E_proposer (EPname)  VALUES (%s)",(company,))
		my_curs.execute("INSERT INTO proposer  VALUES (%s, %s)",(company, userId))
	except:
		pass
	db.commit()
	my_curs.close()
	db.close()
#//////////////////////////////////////// GET Users

def get_users():
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("SELECT userId,username FROM User")
	result = my_curs.fetchall()
	my_curs.close()
	db.close()
	return result
#//////////////////////////////////////// Supprimer un utilisateur(on hold)

def delete_user(userId):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	try:
		my_curs.execute("DELETE FROM user WHERE userId = (%s) ",(userId,))
	except:
		pass
	db.commit()
	my_curs.close()
	db.close()
#//////////////////////////////////////// GET Existing COMPANIES

def get_companies():
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("SELECT Ename,Id_gerant FROM Entreprise")
	result = my_curs.fetchall()
	my_curs.close()
	db.close()
	return result
#//////////////////////////////////////// Supprimer une entreprise(on hold)

def delete_company(company):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("DELETE FROM Entreprise WHERE Ename = (%s) ",(company,))
	db.commit()
	my_curs.close()
	db.close()

#////////////////////// insert data

def insert_data(company, pos, neg, S_words, S_frequincies, S_likes_T, S_retweets_T, max_L,max_R, S_dates,id_M):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	today = date.today()
	S_date = today.strftime("%Y-%m-%d %H:%M:%S")
	my_curs.execute("INSERT INTO company_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s,%s,%s)", (company, pos, neg, S_words, S_frequincies, S_likes_T, S_retweets_T, max_L,max_R, S_dates,id_M,S_date) )
	db.commit()
	my_curs.close()
	db.close()
#//////////////// get data

def get_data(company):
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
	frequincies = data[0][4].split(',')
	likes_T = data[0][5].split(',')
	retweets_T = data[0][6].split(',')
	max_L = data[0][7]
	max_R = data [0][8]
	dates = data[0][9].split(',')
	id_m = data[0][10]
	my_curs.close()
	db.close()
	return(pos, neg, words, frequincies ,likes_T,retweets_T, max_L, max_R,dates,id_m)

#////////////// test exist

def test_data(company):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("SELECT COUNT(*) FROM company_data WHERE company = %s ",(company,))
	i= my_curs.fetchmany(size = 1)
	if (i[0][0] == 0):
		my_curs.close()
		db.close()
		return(0)
	else:
		my_curs.close()
		db.close()
		return(1)

#/////////////// Mise a jour

def Mise_a_jour():
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	today = date.today()
	my_curs.execute("SELECT * FROM company_data")
	items = my_curs.fetchall()
	for item in items:
		if((((today - item[11]).days)*24) >= 24):
			my_curs.execute("DELETE FROM company_data WHERE Timing = (%s) ", (item[11],))
	db.commit()
	my_curs.close()
	db.close()

#//////////////////// get user Id

def get_userId(name, passwd):
	db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")
	my_curs = db.cursor()
	my_curs.execute("SELECT userId FROM User WHERE username = %s AND password = %s", (name,passwd))
	result = my_curs.fetchall()
	my_curs.close()
	db.close()
	return result[0][0]

	


	