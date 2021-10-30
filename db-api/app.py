import model
import os, datetime
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{0}:{1}@{2}/images".format(DB_USER,DB_PASSWORD,DB_HOST)
api = Api(app)

db = SQLAlchemy(app)
marsh = Marshmallow(app)

image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

api.add_resource(ImageResources, "/images")
api.add_resource(ImageResource,'/images/<int:image_id>')