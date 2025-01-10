from typing import Optional, List, Dict, Any
from models.image import Image


def list_images() -> List[Image]:
    return Image.objects()


def find_by_id(image_id: str) -> Optional[Image]:

    try:
        return Image.objects.get(id=image_id)

    except Exception:
        return None


def insert_image(image: Image) -> Optional[Image]:

    try:
        image.save()
        return image

    except Exception:
        return None