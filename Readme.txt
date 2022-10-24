					
					                README 


Réalisateurs : Aarab Ilham 
               Taizoukt Anouar 

Objectif du projet : une application web pour la visualisation de la réputation des entreprises. 
 

prérequis : afin de pouvoir executer l'application sur votre poste vous devez aborder d'installer :
	- voir le fichier requirements.txt 
	- installer mySQL pour importer la base de donnée exporté dans le fichier Dump20210714.sql 
la commande pour l'installation des paquets nécessaires: pip install -r requirements.txt 


Les fichiers de la création de l'application :

	Templates : qui contient tout les fichier html 
	static : qui contient les fichiers css et javascript 
	app.py : qui contient flask et la gestion des interfaces de l'application 
	chart.py : pour la création des histogrammes 
	control.py : pour le calcul de pourcentage des positifs et des négatifs prédictions , ainsi que les 20 mots les plus répetés . 
	models.py : pour la gestion de base de donnée 
	myclass.py : pour l'extraction et l'analyse des tweets. 
	test-db.py : pour la création de la base des données.
	My_trained_model_ar_Ngram_2_1.sav : le model entrainé sauvegardé (sérialisé).
	vectorizerNgram_1_2.sav : le vectorizer sérialisé. 

Le fichier de jeu de données utilisé pour l'entraînement du modèle : 
			Mydata.txt


Execution : pour l'exécution de l'application vous devez lancer la commande suivante : python app.py pour lancer l'application dans localhost. 

Déploiement : 
	Le manager : username : manager 
	             password : 123 
le manager doit se connecter d'abord à travers l'interface administrateur, il  peut accéder à la  base de donnée pour ajouter une entreprise ou bien annuler une entreprise non valide , ou supprimer un utilisateur . 
l'utilisateur : il doit s'authentifier , et créer un compte pour accéder au service de la recherche de la réputation d'une entreprise , il peut aussi proposer une entreprise au système . 
 	les utilisateur qui existe déjà :
		   Anouar : ano 
		   ilham : ila 

	
	

