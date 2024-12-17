from flask import Flask, request
from flask_cors import CORS
from json import dumps
from auxiliary_angle_converter.auxiliary_angle import auxiliary_angle_compute
import sys
app = Flask(__name__)
CORS(app)
port = 5003

@app.route("/calculate", methods=['GET'])
def calculate_auxiliary_angle():
    data = request.args
    return dumps(auxiliary_angle_compute(data.get("expression"), True, int(data.get("decimal_places")), data.get("in_radians")))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, threaded=True)
    
