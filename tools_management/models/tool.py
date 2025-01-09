from mongoengine import Document, StringField # type: ignore

class Tool(Document):


    id = StringField(required=True, primary_key=True)
    input_type = StringField(required=True)
    output_type = StringField(required=True)


    def __repr__(self) -> str:
        return f'<Tool({self.id}>'


    def to_json(self):
        return {
            '_id': self.id,
            'input_type': self.input_type,
            'output_type': self.output_type
        }