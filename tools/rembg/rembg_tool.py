import base64
from rembg import remove
from rembg_message_reply import RembgMessageReply
from rembg_message_request import RembgMessageRequest

class RembgTool:

    def __init__(self, request: RembgMessageRequest) -> None:
        self.request = request

    def apply(self) -> RembgMessageReply:
        input_image_data = base64.b64decode(self.request.getImage())
        
        # Use rembg to remove the background
        output_image_data = remove(input_image_data)
        
        # Return the processed image as a base64-encoded string
        return RembgMessageReply(base64.b64encode(output_image_data).decode('utf-8'))
