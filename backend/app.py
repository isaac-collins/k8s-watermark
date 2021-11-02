import cv2, base64, numpy
from flask import Flask, render_template
from flask import request, jsonify

app = Flask(__name__)

def watermark_image(
    b64_image,
    text
    ):
    
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
    print(encoded_image)
    return encoded_image

@app.route('/backend', methods=['POST','GET'])
def index():
    print(request.json)
    transformed_image = watermark_image(request.json['image'],request.json['text'])
    return jsonify({
        'transformed_image':transformed_image
        })

@app.route('/test')
def test_route():
    return "OK"


