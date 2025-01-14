import base64
from rembg import remove # type: ignore
from autocrop_message_reply import AutoCropMessageReply
from autocrop_message_request import AutoCropMessageRequest

class AutoCropTool:

    def __init__(self, request: AutoCropMessageRequest) -> None:
        self.request = request

    def apply(self) -> AutoCropMessageReply:
        input_image_data = base64.b64decode(self.request.getImage())
        
        # Use rembg to remove the background
        output_image_data = remove(input_image_data)
        
        # Return the processed image as a base64-encoded string
        return AutoCropMessageReply(base64.b64encode(output_image_data).decode('utf-8'))
