from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

account_sid = 'ACc58f8372eb9b75f8d5fe4d587bccd167'
auth_token = '54ed90c4225c224e23f0d35568b307d8'

client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+12055129674',
                              body='body',
                              to='+17326667804'
                          )

print(message.sid)

def initialSMSReply():
    # replying to message 
    resp= MessaginResponse();

    #adding message
    resp.message("Welcome to Rutgers ChatBot! Please specify one of the following options:Events, Busses, Dining, Sports, Recreation, Places, or Schedule of Classes")

    return str(resp)

def branchingFromFirst():
    # getting message user sent to our number
    body = request.values.get('Body', None)

    # initializing our Twiml response
    resp = MessagingResponse()

    # removing white space from end and making string lowercase
    body = body.strip()
    body = body.lower()

    # going through possible cases

