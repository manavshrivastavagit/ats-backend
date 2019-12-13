from flasgger import Swagger
from flask import Flask
from flask.blueprints import Blueprint

import config
import routes
from models import db
from flask_cors import CORS
import os

from flask import Flask, request, abort, jsonify, send_from_directory,send_file


UPLOAD_DIRECTORY = "../static/img/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)



# config your API specs
# you can define multiple specs in the case your api has multiple versions
# ommit configs to get the default (all views exposed in /spec url)
# rule_filter is a callable that receives "Rule" object and
#   returns a boolean to filter in only desired views

server = Flask(__name__)
CORS(server)

@server.route("/static/img")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    STATIC_IMG_DIRECTORY = "./static/img/"
    for filename in os.listdir(STATIC_IMG_DIRECTORY):
        path = os.path.join(STATIC_IMG_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)

@server.route("/download/<path:path>")
def get_file(path):
    """Download a file."""
    DOWNLOAD_DIRECTORY = "../static/img/"
    return send_from_directory(DOWNLOAD_DIRECTORY, path, as_attachment=True)

@server.route("/static/img/<path:path>")
def getfile(path):
    """Download a file."""
    return send_file( "../static/img/"+ path, mimetype='image/jpeg')

server.config["SWAGGER"] = {
    "swagger_version": "2.0",
    "title": "Application",
    "specs": [
        {
            "version": "0.0.1",
            "title": "Application",
            "endpoint": "spec",
            "route": "/application/spec",
            "rule_filter": lambda rule: True,  # all in
        }
    ],
    "static_url_path": "/apidocs",
}

Swagger(server)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(server)
db.app = server

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)
