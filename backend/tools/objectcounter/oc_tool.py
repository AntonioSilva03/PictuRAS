import base64
import numpy as np # type: ignore
import cv2 # type: ignore
from detectron2.engine import DefaultPredictor  # type: ignore
from detectron2.config import get_cfg # type: ignore
from detectron2.model_zoo import get_config_file, get_checkpoint_url # type: ignore
from detectron2.data import MetadataCatalog # type: ignore
from collections import Counter
from oc_message_reply import ObjectCountingMessageReply
from oc_message_request import ObjectCountingMessageRequest

class ObjectCountingTool:

    def __init__(self, request: ObjectCountingMessageRequest) -> None:
        self.request = request

    def apply(self) -> ObjectCountingMessageReply:
        # Decode the image from base64
        image_data = base64.b64decode(self.request.getImage())
        np_arr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Setup Detectron2 configuration
        cfg = get_cfg()
        cfg.merge_from_file(get_config_file("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"))
        cfg.MODEL.WEIGHTS = get_checkpoint_url("COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml")
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # Set a threshold for predictions
        cfg.MODEL.DEVICE = "cuda" if cv2.cuda.getCudaEnabledDeviceCount() > 0 else "cpu"

        # Create a predictor
        predictor = DefaultPredictor(cfg)

        # Perform inference
        outputs = predictor(image)

        # Get the class names from Detectron2's COCO metadata
        metadata = MetadataCatalog.get(cfg.DATASETS.TRAIN[0])
        class_names = metadata.get("thing_classes", [])

        # Extract detected classes
        detected_classes = outputs["instances"].pred_classes.cpu().numpy()
        detected_class_names = [class_names[i] for i in detected_classes]

        # Count occurrences of each class
        object_counts = dict(Counter(detected_class_names))

        # Return the counts as a reply
        return ObjectCountingMessageReply(object_counts)
