class ScaleMessageRequest:

    def __init__(self, image: str, height : int, width : int) -> None:
        self.image = image
        self.height = height
        self.width = width


    def getImage(self) -> str:
        return self.image


    def getHeight(self) -> int:
        return self.height


    def getWidth(self) -> int:
        return self.width


    def to_dict(self) -> dict:
        return {
            'image': self.image,
            'height': self.height,
            'width': self.width
        }


    @staticmethod
    def from_dict(data: dict) -> 'ScaleMessageRequest':
        return ScaleMessageRequest(
            image=data['image'],
            height=data['height'],
            width=data['width']
        )