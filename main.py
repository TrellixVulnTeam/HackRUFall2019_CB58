from twilio.rest import Client

account_sid = 'ACc58f8372eb9b75f8d5fe4d587bccd167'
auth_token = '54ed90c4225c224e23f0d35568b307d8'
client = Client('account_sid','auth_token')


message = client.messages.create(body="Message that will be sent", from_='number from twilio', to='number receiving')

print(message.sid)
