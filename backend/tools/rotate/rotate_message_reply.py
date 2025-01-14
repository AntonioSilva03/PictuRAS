import json

class RotateMessageReply:

    def __init__(self, image: str) -> None:
        self.image = image


    def getImage(self) -> str:
        return self.image


    def to_json(self) -> str:
        return json.dumps({
            'image': self.image,
        })


    @staticmethod
    def from_json(data: str) -> 'RotateMessageReply':
        data = json.loads(data)
        return RotateMessageReply(
            image=data['image'],
        )