from mongoengine import Document, StringField, ListField, EmbeddedDocument, EmbeddedDocumentField, DynamicField # type: ignore


class Parameter(EmbeddedDocument):

    name = StringField(required=True)
    type = StringField(required=True, choices=['int', 'float', 'string', 'hex'])
    value = DynamicField(required=True)
    min_value = DynamicField()
    max_value = DynamicField()


class Tool(Document):

    name = StringField(required=True, unique=True) 
    input_type = StringField(required=True, choices=['image', 'text'])
    output_type = StringField(required=True, choices=['image', 'text'])
    parameters = ListField(EmbeddedDocumentField(Parameter), required=True)

    def to_json(self) -> dict:
        return {
            'name': self.name,
            'input_type': self.input_type,
            'output_type': self.output_type,
            'parameters': [
                {
                    'name': parameter.name,
                    'type': parameter.type,
                    'value': parameter.value,
                    'min_value': parameter.min_value,
                    'max_value': parameter.max_value,
                }
                for parameter in self.parameters
            ],
        }