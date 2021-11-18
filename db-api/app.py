import os, datetime, base64
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import *
from flask_restful import Resource, Api


DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}/images".format(DB_USER,DB_PASSWORD,DB_HOST)

api = Api(app)
db = SQLAlchemy(app)


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(30))
    data = db.Column(db.BINARY) #convert to BLOB

class ImageSchema(Schema):

    id = fields.Integer()
    timestamp = fields.String()
    data = fields.Method("decode_image",deserialize="encode_image")

    def decode_image(self, value):
        return base64.b64decode(value)

    def encode_image(self, value):
        return base64.b64encode(value)



image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

class ImageResources(Resource):
    def get(self):
        images = Images_schema.query.all()
        return images_schema.dump(images)

    def post(self):
        image = Images(
            timestamp = datetime.datetime.now(),
            data = base64.b64decode(request.json["transformed_image"])
        )
        db.session.add(image)
        db.session.commit()
        return data

class ImageResource(Resource):
    def get(self, image_id):
        image = Images.query.get_or_404(image_id)
        return image_schema.dump(image)

api.add_resource(ImageResources, "/images")
api.add_resource(ImageResource,'/images/<int:image_id>')


