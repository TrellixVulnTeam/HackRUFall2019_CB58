from flask import Flask, request, redirect, session
import os
from twilio.twiml.messaging_response import MessagingResponse
#from flask_restful import Resource, Api
#from flask_session import session
import json

app = Flask(__name__)
app.secret_key = "HELLO"
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
userI = None
@app.route('/set/')
def set():
    session['key'] = 'value'
    session['userInput']=userI
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')

@app.route("/sms", methods=['GET', 'POST'])



def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a message
    userInput=(request.form['CurrentInput'])
    resp.message(userInput)
    print(resp)
    return str(resp)
    userI=userInput


if __name__ == "__main__":
    app.run(debug=True)