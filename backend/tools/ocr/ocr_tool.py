import magic
import base64
import subprocess
from ocr_message_reply import OCRMessageReply
from ocr_message_request import OCRMessageRequest

class OCRTool:

    def __init__(self, request : OCRMessageRequest) -> None:
        self.request = request


    def apply(self) -> OCRMessageReply:

        mime = magic.Magic(mime=True)

        tesseract_command = [
            'tesseract',
            '-', '-',
            '-l', 'eng'
        ]

        result = subprocess.run(
            tesseract_command,
            input=base64.b64decode(self.request.getImage()),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )

        return OCRMessageReply(
            mimetype=mime.from_buffer(result.stdout),
            data=base64.b64encode(result.stdout).decode('utf-8'),
        )