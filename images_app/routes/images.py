from io import BytesIO
from flask import Blueprint, request, jsonify, send_file # type: ignore
from models.image import Image
from controllers.image import (
    list_images,
    find_by_id,
    find_info_by_id,
    find_chunks_by_id,
    insert_image,
    delete_image,
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
    return jsonify({'error': 'Image not found'}), 404


@images_blueprint.route('/info/<string:image_id>', methods=['GET'])
def rout_get_image_info(image_id: str):
    image_info = find_info_by_id(image_id)
    if image_info:
        return jsonify(image_info.to_json()), 200
    return jsonify({'error': 'Image not found'}), 404


@images_blueprint.route('/data/<string:image_id>', methods=['GET'])
def rout_get_image_data(image_id: str):
    chunks = find_chunks_by_id(image_id)
    image_info = find_info_by_id(image_id)
    if chunks and image_info:
        data = b''.join(chunk.data for chunk in chunks)
        return send_file(BytesIO(data), mimetype=f'image/{image_info.format.lower()}'), 200
    return jsonify({'error': 'Image not found'}), 404


@images_blueprint.route('/<string:image_id>', methods=['DELETE'])
def rout_delete_image(image_id: str):
    image = delete_image(image_id)
    if image:
        return jsonify({'id': str(image.id)}), 200
    return jsonify({'error': 'Image not found'}), 500


@images_blueprint.route('/', methods=['POST'])
def rout_insert_image():

    try:
        new_image = Image(
            project=request.form.get('project'),
            image=BytesIO(request.files['image'].read())
        )

        image = insert_image(new_image)
        return jsonify(image.to_json()), 200

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500