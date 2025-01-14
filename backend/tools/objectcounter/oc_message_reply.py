import json

class ObjectCountingMessageReply:

    def __init__(self, object_counts: dict) -> None:
        self.object_counts = object_counts

    def getObjectCounts(self) -> dict:
        return self.object_counts

    def to_json(self) -> str:
        return json.dumps({
            'object_counts': self.object_counts,
        })

    @staticmethod
    def from_json(data: str) -> 'ObjectCountingMessageReply':
        data = json.loads(data)
        return ObjectCountingMessageReply(
            object_counts=data['object_counts'],
        )