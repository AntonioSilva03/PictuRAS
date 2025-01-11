import base64
import cv2
import numpy as np
from ultralytics import YOLO
from pc_message_reply import PeopleCountingMessageReply
from pc_message_request import PeopleCountingMessageRequest

class PeopleCountingTool:

    def __init__(self, request: PeopleCountingMessageRequest) -> None:
        self.request = request

    def apply(self) -> PeopleCountingMessageReply:

        # Decode the image from base64
        image_data = base64.b64decode(self.request.getImage())
        np_arr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Load YOLO model
        model = YOLO('yolov8n.pt')  # Use YOLOv8 pretrained model

        # Perform detection
        results = model(image)

        if len(results[0].boxes) == 0:  # No detections
            return PeopleCountingMessageReply(0)

        # Extract bounding boxes, confidence scores, and class IDs
        detections = results[0].boxes.xywh.cpu().numpy()  # Shape: [N, 4]
        confidences = results[0].boxes.conf.cpu().numpy()  # Shape: [N]
        class_ids = results[0].boxes.cls.cpu().numpy()  # Shape: [N]

        # Filter detections for 'person' class (COCO class ID 0)
        person_count = sum(1 for class_id in class_ids if int(class_id) == 0)

        # Return the count as a reply
        return PeopleCountingMessageReply(person_count)