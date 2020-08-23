from flask import Flask, jsonify, request

app = Flask(__name__)
    
@app.route('/health')
def health():
    return 'ok'

# @app.route('/post', methods=['POST'])
@app.route('/getGraphInfo')
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

# MOCK
def create_1day():
	return [
		{
		    "name": "ms",
		    "ticker": "MSFT",
		    "value": 5.3,
		    "unit": "%"
		},{
		    "name": "apple",
		    "ticker": "AAPL",
		    "value": -10,
		    "unit": "%"
		}
	]

def create_1week():
	return [
		{
		    "name": "ms",
		    "ticker": "MSFT",
		    "value": 10.3,
		    "unit": "%"
		},{
		    "name": "apple",
		    "ticker": "AAPL",
		    "value": -20,
		    "unit": "%"
		}
	]

def create_per():
	return [
		{
		    "name": "ms",
		    "ticker": "MSFT",
		    "value": 5.3,
		    "unit": ""
		},{
		    "name": "apple",
		    "ticker": "AAPL",
		    "value": 33,
		    "unit": ""
		}
	]

def create_pbr():
	return [
		{
		    "name": "ms",
		    "ticker": "MSFT",
		    "value": 44.3,
		    "unit": ""
		},{
		    "name": "apple",
		    "ticker": "AAPL",
		    "value": 12.4,
		    "unit": ""
		}
	]