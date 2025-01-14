import json

class PeopleCountingMessageReply:
    def __init__(self, people_count: int) -> None:
        self.people_count = people_count

    def getPeopleCount(self) -> int:
        return self.people_count

    def to_json(self) -> str:
        return json.dumps({'people_count': self.people_count})

    @staticmethod
    def from_json(data: str) -> 'PeopleCountingMessageReply':
        data = json.loads(data)
        return PeopleCountingMessageReply(people_count=data['people_count'])
