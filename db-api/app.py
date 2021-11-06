import os, datetime, base64
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api


DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{0}:{1}@{2}/images".format(DB_USER,DB_PASSWORD,DB_HOST)
api = Api(app)

db = SQLAlchemy(app)
marsh = Marshmallow(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(30))
    data = db.Column(db.BLOB)

class ImageSchema(marsh.Schema):
    class Meta:
        fields = ("id","timestamp","data")
        model = Image

image_schema = ImageSchema()
images_schema = ImageSchema(many=True)

def dump_with_b65(schema_obj,obj):
    data = schema_obj.dump(obj)
    data.update({
        "data": base64.b64encode(data["data"])
    })
    return data

class ImageResources(Resource):
    def get(self):
        images = Image.query.all()
        return images_schema.dump(images)

    def post(self):
        image = Image(
            timestamp = datetime.datetime.now(),
            data = base64.b64decode(request.json["data"])
        )
        db.session.add(image)
        db.session.commit()
        return image_schema.dump(image)

class ImageResource(Resource):
    def get(self, image_id):
        image = Image.query.get_or_404(image_id)
        return image_schema.dump(image)

api.add_resource(ImageResources, "/images")
api.add_resource(ImageResource,'/images/<int:image_id>')
