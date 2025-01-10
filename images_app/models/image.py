from mongoengine import Document, StringField, ImageField # type: ignore


class Image(Document):
    owner = StringField(required=True)
    image = ImageField(size=(1920, 1080, True),required=True)