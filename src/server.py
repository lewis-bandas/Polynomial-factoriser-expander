from flask import Flask, request
from flask_cors import CORS
from json import dumps
from auxiliary_angle_converter.auxiliary_angle import auxiliary_angle_compute
import sys
APP = Flask(__name__)
CORS(APP)
port = 5003

@APP.route("/calculate", methods=['GET'])
def calculate_auxiliary_angle():
    data = request.args
    return dumps(auxiliary_angle_compute(data.get("expression"), True, int(data.get("decimal_places"))))
    
if __name__ == "__main__":
    APP.run(host='172.19.92.80', port=port, threaded=True)
    
