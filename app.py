from flask import Flask
from flask_cors import CORS
import requests
import json
import twistlock 


app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route('/',methods=['GET'])
def default():
    return {
         "message": "Hello World! I'm the Lucky API!"
    }

name = "test"

@app.route('/selam',methods=['GET'])
def selam():
    return {
         "message": "Hello " +name+ "! I'm the Lucky API!"
    }


@app.route('/lucky',methods=['GET'])
def magic():
    response = requests.get(url="http://test.com/magic", headers={'Content-Type': 'application/json'})
    deserialized = json.loads(response.text)
    magic_value = deserialized["data"]
    return {
        "message": "I'm happy to get magic-number: "+ str(magic_value) +". I'm the luckiest API :)"
    }


@app.route('/defenders',methods=['GET'])
def twistlock_defenders():
    return twistlock.call_twistlock_defenders()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)