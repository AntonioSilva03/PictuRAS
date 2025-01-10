import math
import base64
import subprocess
from rotate_message_reply import RotateMessageReply
from rotate_message_request import RotateMessageRequest

class RotateTool:

    def __init__(self, request : RotateMessageRequest) -> None:
        self.request = request


    def apply(self) -> RotateMessageReply:

        angle = - self.request.getAngle() * math.pi / 180

        ffmpeg_command = [
            'ffmpeg',
            '-i', '-',
            '-vf', f'rotate={angle}:ow=rotw({angle}):oh=roth({angle})',
            '-preset', 'ultrafast',
            '-f', 'image2', '-'
        ]

        result = subprocess.run(
            ffmpeg_command,
            input=base64.b64decode(self.request.getImage()),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )

        return RotateMessageReply(base64.b64encode(result.stdout).decode('utf-8'))