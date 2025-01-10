import os
from flask import Flask # type: ignore
from mongoengine import connect # type: ignore
from routes.images import images_blueprint

app = Flask(__name__)

connect(
    db=os.getenv('PICTURAS_DB','picturas'),
    host=os.getenv('MONGO_HOST','localhost'),
    port=int(os.getenv('MONGO_PORT', 27017)))

app.register_blueprint(images_blueprint, url_prefix='/images')

if __name__ == '__main__':
    app.run(
        host=os.getenv('IMAGES_FLASK_HOST', '0.0.0.0'),
        port=int(os.getenv('IMAGES_FLASK_PORT', 6000)),
        debug=True
    )