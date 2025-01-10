from mongoengine import Document, ImageField, StringField, IntField, LongField, ObjectIdField, DateTimeField, BinaryField # type: ignore


class ImageChunk(Document):
    
    meta = {'collection': 'images.chunks'}

    files_id = ObjectIdField()
    n = IntField()
    data = BinaryField()

    def to_json(self) -> dict:
        return {
            '_id': str(self.id),
            'files_id': str(self.files_id),
            'n': self.n,
            'data': self.data,
        }


class ImageFile(Document):
    
    meta = {'collection': 'images.files'}

    width = IntField()
    height = IntField()
    format = StringField()
    thumbnail_id = ObjectIdField()
    chunkSize = IntField()
    length = LongField()
    uploadDate = DateTimeField()

    def to_json(self) -> dict:
        return {
            '_id': str(self.id),
            'width': self.width,
            'height': self.height,
            'format': self.format,
            'chunkSize': self.chunkSize,
            'length': self.length,
            'uploadDate': str(self.uploadDate),
        }


class Image(Document):

    meta = {'collection': 'image'}

    project = StringField(required=True)
    image = ImageField(size=(1920, 1080, True),required=True)

    def to_json(self) -> dict:
        return {
            '_id': str(self.id),
            'project': self.project,
            'image': str(self.image._id),
        }