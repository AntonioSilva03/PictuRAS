from enum import Enum
from mongoengine import Document, StringField, EnumField, signals # type: ignore
from werkzeug.security import generate_password_hash # type: ignore


class UserType(Enum):
    ANONYMOUS = 'anonymous'
    REGISTERED = 'registered'


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    name = StringField(required=True)
    email = StringField(required=True)
    type = EnumField(UserType, required=True)


    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if document.password and not document.password.startswith("pbkdf2:"):
            document.password = generate_password_hash(document.password)


    def to_json(self) -> dict:
        return {
            'username' : self.username,
            'name': self.name,
            'email': self.email,
            'type': self.type.value 
        }


signals.pre_save.connect(User.pre_save, sender=User)