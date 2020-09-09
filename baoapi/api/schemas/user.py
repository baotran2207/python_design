from baoapi.models import User, TokenBlacklist
from baoapi.extensions import ma, db
from marshmallow import fields, validate


class BaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = db.session


class UserSchema(BaseSchema):
    
    id = ma.String(dump_only=True)
    password = ma.String(load_only=True, required=True)
    email = fields.Email(required=True)

    # exp_token = fields.Nested(BlacklistSchema)
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

class BlacklistSchema(BaseSchema):

    id = ma.String()
    jti = ma.String()
    token_type = ma.String()
    revoked = ma.Boolean()

    user = fields.Nested(UserSchema)
    class Meta:
        model = TokenBlacklist
        load_instance = True

