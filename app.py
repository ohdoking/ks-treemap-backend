from flask import Flask, jsonify, request
from flask_cors import CORS
from mock import *

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/health')
def health():
    return 'ok'

# @app.route('/post', methods=['POST'])
@app.route('/api/v1/getGraphInfo')
def getGraphInfo():
	type = request.args.get('type')
	d = None
	if type == "1day":
		d = create_1day()
	elif type == "1week":
		d = create_1week()
	elif type == "per":
		d = create_per()
	elif type == "pbr":
		d = create_pbr()
	else:
		d = create_1day()

	return jsonify(d)

