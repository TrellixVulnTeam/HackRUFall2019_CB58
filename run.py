from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(requst.)

    return str(resp)
#@app.route("/sms", methods=['GET'])
if request.method=='POST':
    return request.form.get('keywords')

if __name__ == "__main__":
    app.run(debug=True)