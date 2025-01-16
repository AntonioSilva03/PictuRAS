import base64
import numpy as np
import cv2
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
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

        # Set up Detectron2 model configuration
        cfg = get_cfg()
        cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
        cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # Confidence threshold
        cfg.MODEL.ROI_HEADS.NUM_CLASSES = 80

        predictor = DefaultPredictor(cfg)

        # Perform detection
        outputs = predictor(image)

        # Extract class IDs and count 'person' detections (COCO ID 0)
        class_ids = outputs["instances"].pred_classes.cpu().numpy()
        person_count = sum(1 for class_id in class_ids if class_id == 0)

        # Return the count as a reply
        return PeopleCountingMessageReply(person_count)
