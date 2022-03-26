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

#
#Image object model
# 
class Images(db.Model):

    def __init__(self, b64data):
        self.data = base64.b64decode(b64data)
        self.timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(30))
    data = db.Column(db.BINARY) 

#
#Marsh schema
#
class ImageSchema(Schema):
    id = fields.Integer()
    timestamp = fields.String()
    data = fields.Method("encode_image", deserialize="decode_image")

    #convert bytes from db to b64 str
    def encode_image(self, obj):
        return base64.b64encode(obj.data).decode("utf-8")

    #convert b64 string from client to bytes 
    def decode_image(self, obj):
        return base64.b64decode(obj.data)

image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

#
#Flask_Restful resources
#
class ImageResources(Resource):
    def get(self):
        images = Images.query.all()
        return images_schema.dump(images)

    def post(self):
        image_obj = Images(
            b64data = request.json["transformed_image"]
        )
        db.session.add(image_obj)
        db.session.commit()
        return image_schema.dump(image_obj)

class ImageResource(Resource):
    def get(self, image_id):
        image = Images.query.get_or_404(image_id)
        return image_schema.dump(image)

api.add_resource(ImageResources, "/images")
api.add_resource(ImageResource, "/images/<int:image_id>")


