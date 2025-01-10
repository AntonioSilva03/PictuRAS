import os
from flask import Flask # type: ignore
from mongoengine import connect # type: ignore
from routes.tools import tools_blueprint

app = Flask(__name__)

connect(
    db=os.getenv('PICTURAS_DB','picturas'),
    host=os.getenv('MONGO_HOST','localhost'),
    port=int(os.getenv('MONGO_PORT', 27017)))

app.register_blueprint(tools_blueprint, url_prefix='/tools')

if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_PORT', 5000)),
        debug=True
    )