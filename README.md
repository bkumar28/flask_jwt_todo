# Simple todo flask-restful app for jwt login authentication
This is small todo jwt login authentication app. it allows the user to Signup, Reset password, Login and Logout.
The user also perform crud operation after login like add new user, get list of user, update user and delete user.

# Requirements

  [Python3](https://www.python.org/downloads/), [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/), [Flask Restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html), [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/), [Postgresql](https://www.postgresql.org/docs/) and [SqlAlchemy](https://docs.sqlalchemy.org/en/13/).

## Installation

 create virtual environment

``` 
virtualenv -p python3 venv
```

activate virtual environment

```
. venv/bin/activate
```

install dependencies

```
pip3 install -r requirement.txt
```

generate secret key

```
(venv) python3
>>>import os
>>>os.urandom(24)
```

install and create psql database

https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e


create database table by [Alembic](https://flask-migrate.readthedocs.io/en/latest/)

 ```
 python3 manage.py db init
 python3 manage.py db migrate
 python3 manage.py db upgrade
 ```

create database table manually

```
(venv) python3
from app.app import create_app, db
app = create_app()
app.app_context().push()
db.init_app(app)
db.create_all()
db.session.commit()
```

  get flask port  

 ```
 sudo netstat -tulnp | grep :5000
 ```
