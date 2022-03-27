import cv2, base64, numpy, requests
from flask import Flask, render_template, request, jsonify

db_api = "http://db-api-svc/"
app = Flask(__name__)

#
# convert b64 to cv2 img array, add user text, return new b64 image
#
def watermark_image(b64_image, text):
    img_bytes = base64.b64decode(b64_image)
    image_array = numpy.frombuffer(img_bytes,dtype=numpy.uint8)
    img = cv2.imdecode(image_array,flags=cv2.IMREAD_COLOR)
    font = cv2.FONT_HERSHEY_COMPLEX
    org = (00,100)
    color = (0,0,255)
    img = cv2.putText(img, text, org, font,1,color,2,cv2.LINE_AA,False)
    retval, buffer = cv2.imencode('.jpg', img)
    encoded_image = base64.b64encode(buffer)
    encoded_image = encoded_image.decode("utf-8")

    return encoded_image

@app.route('/backend', methods=['POST','GET'])
def index():
    transformed_image = watermark_image(request.json['image'],request.json['text'])

    # send transformed image back to frontend
    response = {
        'transformed_image': transformed_image
    }
    # send transformed image to db for storage
    req_data = requests.post(
        db_api + "images",
        json = {'transformed_image': transformed_image},
    )
    return jsonify(response)