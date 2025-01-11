from typing import Optional, List
from models.image import Image, ImageFile, ImageChunk
import traceback


def list_images() -> List[Image]:
    return Image.objects()


def find_by_id(image_id: str) -> Optional[Image]:
    try:
        return Image.objects.get(id=image_id)
    except Exception:
        return None


def find_info_by_id(image_id: str) -> Optional[ImageFile]:
    try:
        image = Image.objects.get(id=image_id)
        return ImageFile.objects.get(id=image.image._id)
    except Exception:
        traceback.print_exc()
        return None
    

def find_chunks_by_id(image_id) -> Optional[List[ImageChunk]]:
    try:
        image = Image.objects.get(id=image_id)
        return ImageChunk.objects.filter(files_id=image.image._id).order_by('n')
    except Exception:
        traceback.print_exc()
        return None


def insert_image(image: Image) -> Optional[Image]:
    try:
        image.save()
        return image
    except Exception:
        return None


def delete_image(image_id: str) -> Optional[Image]:
    try:
        image = Image.objects.get(id=image_id)
        image.delete()
        return image
    except Exception:
        return None