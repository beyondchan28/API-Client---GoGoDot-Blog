from flask import Flask
from flask.templating import render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    url = "http://localhost:8000/resource/"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkBleGFtcGxlLmNvbSIsImV4cCI6MTY0MjMyMTExOX0.ww2t8QeCXL-LSfiw5EOWqYrKDySVLSCf0w0znGRD5s8"
        }

    req = requests.request("GET", url, headers=headers)
    data = json.loads(req.content)

    return render_template('index.html', data= data)

@app.route('/news', methods=['GET'])
def news():
    url = "http://localhost:5000/news/"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkBnbWFpbC5jb20iLCJleHAiOjE2NDI0MDEyMjR9.Yhe8UXawzdexCvf8McqkslBIqC41xt8uaWjmC0y9Dwo"
        }

    req = requests.request("GET", url, headers=headers)
    data = json.loads(req.content)

    return render_template('news.html', data= data)