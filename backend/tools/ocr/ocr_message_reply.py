import json

class OCRMessageReply:

    def __init__(self, text: str) -> None:
        self.text = text


    def getText(self) -> str:
        return self.text


    def to_json(self) -> str:
        return json.dumps({
            'text': self.text,
        })


    @staticmethod
    def from_json(data: str) -> 'OCRMessageReply':
        data = json.loads(data)
        return OCRMessageReply(
            text=data['text'],
        )