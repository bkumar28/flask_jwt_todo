import os
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from app.models.user import User


db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "\x88\x8fG\xd4\x0c\xaao<\xb7\x99\x0c\xe18\x99\x1bF\x9c+\xd9\x8b\x0b\xa7|\xde"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://test:test@localhost/test"

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    db.create_all()