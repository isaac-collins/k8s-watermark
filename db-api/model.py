
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(30))
    data = db.Column(db.String(255))

class ImageSchema(marsh.Schema):
    class Meta:
        fields = ("id","timestamp","data")
        model = Image

class ImageResources(Resource):
    def get(self):
        images = Image.query.all()
        return images_schema.dump(images)

    def post(self):
        image = Image(
            timestamp = datetime.datetime.now()
            data = request.json["data"]
        )
        db.session.add(image)
        db.session.commit()
        return image_schema(image)

class ImageResource(Resource):
    def get(self, image_id):
        image = Image.query.get_or_404(image_id)
        return image_schema.dump(image)