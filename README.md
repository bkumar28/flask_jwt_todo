Pre Reuirement 

Python3, Flask, Flask Restful, Postgresql and SqlAlchemy


Create virtual environment

>>> virtualenv -p python3 venv

Activate virtual environment

>>> . venv/bin/activate

Install dependencies

>>> pip3 install -r requirement.txt


Generate secret key

(venv) python3
>>>import os
>>> os.urandom(24)

Install and Create psql database

https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e


Create database table by Alembic 
Reference : https://flask-migrate.readthedocs.io/en/latest/

>>> python3 manage.py db init
>>> python3 manage.py db migrate
>>> python3 manage.py db upgrade

Create database table manually

(venv) python3
>>> from project import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.init_app(app)
>>> db.create_all()
>>> db.session.commit()

Get flask port  

>>> sudo netstat -tulnp | grep :5000
