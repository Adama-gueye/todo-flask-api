Description
Ce projet est une API REST en Flask pour gérer des tâches (ToDo List), avec :

* Création, mise à jour, suppression de tâches

* Priorité (low, medium, high)

* Pagination des résultats

* Sécurité via clé API

Prérequis
Assure-toi d’avoir installé :

Python 3.8+

MySQL/MariaDB

Pip (gestionnaire de paquets Python)

git clone https://github.com/ton-utilisateur/todo-flask-api.git
cd APIREST

Installation

Installation
Clone le projet (ou copie les fichiers) 

git clone https://github.com/ton-utilisateur/todo-flask-api.git
cd todo-flask-api

Crée un environnement virtuel

python -m venv venv

Installe les dépendances 

pip install -r requirements.txt

Creer la base de donnée
CREATE DATABASE todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

Configure la base de données
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/todo_db"


Execution

python app.py
http://127.0.0.1:5000


 Méthode  Endpoint       Description   
 *************************************                     
 GET      `/tasks`       Liste des tâches (avec pagination) 
 GET      `/tasks/<id>`  Détails d’une tâche                
 POST     `/tasks`       Créer une tâche                    
 PUT      `/tasks/<id>`  Modifier une tâche                 
 DELETE   `/tasks/<id>`  Supprimer une tâche                
 GET      `/tasksdone`   Liste des tâches terminées         

Technologies utilisées
Flask

SQLAlchemy

MySQL

Python 3

REST API
