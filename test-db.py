import mysql.connector
from datetime import date
from datetime import datetime

db = mysql.connector.connect(host="localhost",
							user="root",
							passwd="azerty",
							database = "test_db")

my_curs = db.cursor()


#creating a table
#my_curs.execute("CREATE TABLE User (username VARCHAR(20),password VARCHAR(20), userId int PRIMARY KEY AUTO_INCREMENT )")
#my_curs.execute("CREATE TABLE gerant (manager_name VARCHAR(20),password VARCHAR(20), Id_gerant int PRIMARY KEY AUTO_INCREMENT )")
#my_curs.execute("CREATE TABLE Entreprise (Ename VARCHAR(20)  PRIMARY KEY, Id_gerant int DEFAULT 1)")
#my_curs.execute("CREATE TABLE chercher (Ename VARCHAR(20), userId int)")
#my_curs.execute("ALTER TABLE chercher  ADD CONSTRAINT PK PRIMARY KEY (Ename,userId)")
#my_curs.execute("CREATE TABLE E_proposer (EPname VARCHAR(20)  PRIMARY KEY, Id_gerant int)")
#my_curs.execute("CREATE TABLE propeser (EPname VARCHAR(20), userId int) ")
#my_curs.execute("ALTER TABLE proposer  ADD CONSTRAINT PK2 PRIMARY KEY (EPname,userId)") 
#my_curs.execute("INSERT INTO gerant (manager_name, password) VALUES (%s,%s)", ('Manager', '123') )
#my_curs.execute("INSERT INTO Person (name ,age) VALUES (%s,%s)", ("SKAFANDRI",20))

#my_curs.execute("CREATE TABLE company_data (company VARCHAR(20) PRIMARY KEY, pos float, neg float, S_words VARCHAR(255), S_frequincies VARCHAR(255), S_likes_T VARCHAR(255), S_retweets_T VARCHAR(255) , max_L int, max_R int , S_dates VARCHAR(255),id_M VARCHAR(255))")
#my_curs.execute("DROP table Proposer ")
#my_curs.execute("ALTER TABLE company_data  Modify CONSTRAINT FK_KEY6  FOREIGN KEY (company) REFERENCES Entreprise(Ename) on delete cascade; " )
#my_curs.execute("ALTER TABLE company_data  Modify S_dates VARCHAR(6000) " )

"""

my_curs.execute("SELECT COUNT(*)  FROM Person where personId=2")
i= my_curs.fetchmany(size = 1)
if (i[0] == 0):
	print("not exist")
else:
	print("exist")
	"""
"""
#################################### SIGN UP
util = input("Donner un nom d'utilisateur\n")
passwd = input("Mot de pass\n")
confirm_passwd = input("Confirmer votre mot de pass\n")
if(passwd != confirm_passwd):
	print("votre confirmation n'est pas valide")
else:
	my_curs.execute("INSERT INTO User (username, password) VALUES (%s,%s)",(util, passwd))
"""
######################################	LOG IN
"""
util = input("Donner un nom d'utilisateur\n")
passwd = input("Mot de pass\n")

my_curs.execute("SELECT COUNT(*) FROM User WHERE username = %s AND password = %s ",(util,passwd) )
i= my_curs.fetchmany(size = 1)
if (i[0][0] == 0):
	print("usern*
	ame or password is wrong")
else:
	print("Logged in succefully")
"""
###########################################Insertion a la table Entreprise
"""
my_curs.execute("INSERT INTO Entreprise (Ename) VALUES ('maroc telecom')")
my_curs.execute("SELECT * FROM Entreprise")"""
###########################################Insertion a la table Entreprise Proposé
"""
my_curs.execute("INSERT INTO E_proposer (EPname, Id_gerant) VALUES ('inwi' ,1)")
my_curs.execute("SELECT * FROM E_proposer")
for i in my_curs:
	print(i)"""
##################### INSERTION  a la tableau propeser
"""name = "inwi"
ide = 1
my_curs.execute("INSERT INTO proposer (EPname,userId) VALUES (%s,%s)", (name, ide))"""

##################### INSERTION  a la tableau chercher
"""
#name = "maroc telecom"
#ide = 1
#my_curs.execute("INSERT INTO chercher (Ename,userId) VALUES (%s,%s)", (name, ide))"""
#################################### AJOUTER UN GERANT
"""util = input("Donner un nom d'utilisateur\n")
passwd = input("Mot de pass\n")
confirm_passwd = input("Confirmer votre mot de pass\n")
if(passwd != confirm_passwd):
	print("votre confirmation n'est pas valide")
else:
	my_curs.execute("INSERT INTO gerant (manager_name, password) VALUES (%s,%s)",(util, passwd))"""
today = date.today()
#current_date = today.strftime("%Y-%m-%d %H:%M:%S")
#my_curs.execute("SELECT * FROM company_data")
#my_curs.execute("SELECT userId FROM User WHERE username = %s AND password = %s", ("anouar","ano"))
my_curs.execute("SELECT * FROM proposer")
"""string = "1,2,3"
#a = my_curs.fetchall()
words = string.split(',')
print(words)"""
a = my_curs.fetchall()

print(a)
"""if (item[11] != None and item[11] < today):
		#my_curs.execute("DELETE FROM company_data WHERE Timing = (%s) ", item[11])
		my_curs.execute("SELECT * FROM company_data WHERE Timing = (%s) ", (item[11],))
		a = my_curs.fetchall()"""




db.commit()
my_curs.close()
db.close()