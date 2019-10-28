from datetime import datetime

from app.app import db

class RevokedToken(db.Model):
    """ Stored user blacklisted access token """

    __tablename__ = 'revoked_tokens'

    id = db.Column(db.Integer, primary_key=True)
    user_identity = db.Column(db.String(120), nullable=False)
    jti = db.Column(db.String(520))
    expires = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)