import datetime
from mongoengine import Document, StringField, DateTimeField # type: ignore


class Project(Document):

    meta = {'collection': 'projects'}

    name = StringField(required=True)
    owner = StringField(required=True)
    date = DateTimeField(default=datetime.datetime.now())

    def to_json(self) -> dict:
        return {
            'id': str(self.id),
            'name': self.name,
            'owner': self.owner,
            'date': str(self.date),
        }