import factory
from baoapi.models import User
from uuid import uuid4

class UserFactory(factory.Factory):

    id = factory.Sequence(lambda n: str(uuid4()))
    username = factory.Sequence(lambda n: "user%d" % n)
    email = factory.Sequence(lambda n: "user%d@mail.com" % n)
    password = "mypwd"

    class Meta:
        model = User
