from twilio.rest import Client
import urllib.request

contents = urllib.request.urlopen("http://example.com/foo/bar").read()

account_sid = 'ACc58f8372eb9b75f8d5fe4d587bccd167'
auth_token = '54ed90c4225c224e23f0d35568b307d8'

client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+12055129674',
                              body='Welcome to RUHelp',
                              to='+17326667804'
                          )

print(message.sid)
print(contents)
