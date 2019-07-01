import send, json
from flask import Flask, jsonify, request
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])

def index():
	if (request.method == 'POST'):
		some_json = request.get_json()
		send.send_email(some_json['location']['address'],some_json['date'],
						some_json['description'],some_json['image'])
		return jsonify({"Confirmation": "Submitted!"}), 201
	else:
		return jsonify({"About": "Please make a post-request."}) #"Hello em"

if __name__== "__main__":
	app.debug=True
	app.run()