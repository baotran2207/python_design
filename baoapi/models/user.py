from baoapi.extensions import db, pwd_context
from baoapi.models.BaseModel import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


def gen_uuid():
    return str(uuid.uuid4())
class User(db.Model):
    """Basic user model
    """
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True, default=gen_uuid)
    
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def __repr__(self):
        return "<User %s %s >" % (self.username, self.id)
    
class TokenBlacklist(db.Model):
    """Blacklist representation
    """
    __tablename__ = 'tokenBlacklist'

    id = db.Column(db.String, primary_key=True, default=gen_uuid)
    jti = db.Column(db.String(36), nullable=False, unique=True)
    token_type = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.String, db.ForeignKey("user.id"), nullable=False)
    revoked = db.Column(db.Boolean, nullable=False)
    expires = db.Column(db.DateTime, nullable=False)
    
    user = db.relationship("User", foreign_keys=[user_id])

    def to_dict(self):
        return {
            "token_id": self.id,
            "jti": self.jti,
            "token_type": self.token_type,
            "user_identity": self.user_identity,
            "revoked": self.revoked,
            "expires": self.expires,
        }
