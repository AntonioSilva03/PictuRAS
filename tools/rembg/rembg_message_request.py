import json

class RembgMessageRequest:

    def __init__(self, image: str) -> None:
        self.image = image

    def getImage(self) -> str:
        return self.image

    def to_json(self) -> str:
        return json.dumps({
            'image': self.image,
        })

    @staticmethod
    def from_json(data: str) -> 'RembgMessageRequest':
        data = json.loads(data)
        return RembgMessageRequest(
            image=data['image'],
        )