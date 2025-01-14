import json

class WatermarkMessageReply:

    def __init__(self, image: str) -> None:
        self.image = image

    def getImage(self) -> str:
        return self.image

    def to_json(self) -> str:
        return json.dumps({
            'image': self.image,
        })

    @staticmethod
    def from_json(data: str) -> 'WatermarkMessageReply':
        data = json.loads(data)
        return WatermarkMessageReply(
            image=data['image'],
        )
