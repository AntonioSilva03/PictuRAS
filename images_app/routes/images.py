from io import BytesIO
from flask import Blueprint, request, jsonify # type: ignore
from models.image import Image
from controllers.image import (
    list_images,
    find_by_id,
    insert_image,
)

import traceback

images_blueprint = Blueprint('image', __name__)


@images_blueprint.route('/', methods=['GET'])
def rout_get_images():
    images = list_images()
    return jsonify([image.to_json() for image in images]), 200


@images_blueprint.route('/<string:image_id>', methods=['GET'])
def rout_get_image(image_id: str):
    image = find_by_id(image_id)
    if image:
        return jsonify(image.to_json()), 200
    return jsonify({"error": "Image not found"}), 404


@images_blueprint.route('/', methods=['POST'])
def rout_insert_image():

    try:

        new_image = Image(
            owner=request.form.get('owner'),
            image=BytesIO(request.files['image'].read())
        )

        image = insert_image(new_image)
        return jsonify(image.to_json()), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500