from flask import Flask,render_template,request
import requests

app = Flask(__name__)

endpoint = 'http://backend-svc/x'

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/req',methods=['POST','GET'])
def req():
    print(request.form['image'],request.form['text'])

    data = {
        'text': request.form['text'],
        'image': request.form['image']
    }
    resp = requests.post(endpoint, data)
    return render_template('req.html',data=resp.text)

@app.route('/test')
def test():
    return "OK"
