class ScaleMessageReply:

    def __init__(self, image: str) -> None:
        self.image = image

    
    def getImage(self) -> str:
        return self.image


    def to_dict(self) -> dict:
        return {
            'image': self.image
        }


    @staticmethod
    def from_dict(data) -> 'ScaleMessageReply':
        return ScaleMessageReply(
            image=data['image']
        )