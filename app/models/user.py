from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256

from app.app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    is_activated = db.Column(db.Boolean, default=False)
    last_login = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)  
    create_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    write_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def __init__(self, data):

        self.email_address = data.get('email_address')
        self.password = self.generate_hash(data.get('password'))
        self.firstname = data.get('firstname')
        self.lastname = data.get('lastname')
        self.is_activated = True
        self.create_at = datetime.utcnow()
        self.write_at = datetime.utcnow()

    @classmethod
    def find_by_email_address(cls, email_address):
        return cls.query.filter_by(email_address=email_address).first()

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update_user(self, **data):
        for key, item in data.items():
            if key == 'password':
                setattr(self, key, self.generate_hash(item))
            else:
                setattr(self, key, item)

        self.modified_at = datetime.utcnow()
        db.session.commit()

    @classmethod
    def delete_user(csl,user_id):
        usr = csl.query.filter_by(id=user_id).one()
        db.session.delete(usr)
        db.session.commit()
        return csl

    @staticmethod
    def get_all_users():
        users = User.query.all()

        josn_data = [ { 'firstname' : x.firstname,
                        'lastname' : x.lastname,
                        'email_address' : x.email_address,
                        'is_activated' : x.is_activated
                        } for x in users ] 

        return josn_data

    def __repr(self):
        return '<id {}>'.format(self.id)