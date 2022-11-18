#!venv/bin/python3

from flask import Flask, json, request
from dotenv import load_dotenv
from twilio.rest import Client
import os
import requests
from twilio.twiml.messaging_response import MessagingResponse


load_dotenv()
app = Flask(__name__)
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


@app.route("/")
def hello_world():
    return "<div style=\"height=500px;width=100px\"></div><div><input></input><button>Send</button></div>"


@app.route("/messages/outbound", methods=["POST"])
def create_message():
    args = request.args
    message = client.messages.create(
        from_='+15166146746',
        body=args['body'],
        to='+' + args['to_number']
    )
    response = app.response_class(
        response=json.dumps({'sid': message.sid}),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/messages/inbound", methods=["POST"])
def receive_message():
    args = request.form
    print(args)
    return str(MessagingResponse())
