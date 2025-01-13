from enum import Enum
from mongoengine import Document # type: ignore
from mongoengine.fields import StringField, ListField, EmbeddedDocument, EmbeddedDocumentField, DynamicField, EnumField # type: ignore


class InputOutputType(Enum):
    IMAGE = 'image'
    TEXT = 'text'


class ParameterType(Enum):
    INT = 'int'
    FLOAT = 'float'
    STRING = 'string'
    HEX = 'hex'


class Parameter(EmbeddedDocument):
    name = StringField(required=True)
    type =  EnumField(ParameterType, required=True)
    value = DynamicField(required=True)
    min_value = DynamicField()
    max_value = DynamicField()

    def to_json(self) -> dict:
        return {
            'name': self.name,
            'type': self.type.value,
            'value': self.value,
            'min_value': self.min_value,
            'max_value': self.max_value,
        }


class Tool(Document):

    meta = {'collection': 'tools'}

    name = StringField(required=True, unique=True) 
    input_type = EnumField(InputOutputType, required=True)
    output_type = EnumField(InputOutputType, required=True)
    parameters = ListField(EmbeddedDocumentField(Parameter), required=True)

    def to_json(self) -> dict:
        return {
            'id': str(self.id),
            'name': self.name,
            'input_type': self.input_type.value,
            'output_type': self.output_type.value,
            'parameters': [parameter.to_json() for parameter in self.parameters],
        }