import os
from flask import Flask # type: ignore
from mongoengine import connect # type: ignore
from routes.tools import tools_blueprint

app = Flask(__name__)

connect(
    db=os.getenv('TOOLS_DB','picturas-tools'),
    host=os.getenv('DB_HOST','localhost'),
    port=os.getenv('DB_PORT', 27017))

app.register_blueprint(tools_blueprint, url_prefix='/tools')

if __name__ == '__main__':
    app.run(debug=True)