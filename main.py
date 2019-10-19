from twilio.rest import Client
import urllib.request
import feedparser

contents = urllib.request.urlopen("http://ruevents.rutgers.edu/events/getEventsRss.xml?numberOfDays=7").read()
feed = feedparser.parse('http://ruevents.rutgers.edu/events/getEventsRss.xml?numberOfDays=7')

account_sid = 'ACc58f8372eb9b75f8d5fe4d587bccd167'
auth_token = '54ed90c4225c224e23f0d35568b307d8'

client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               from_='+12055129674',
#                               body='Welcome to RUHelp',
#                               to='+17326667804'
#                           )

# print(message.sid)
# print(contents)
print(str(len(feed['entries'])) + " events happening this week.")

# for x in feed.entries:
#     print (x.title)

print('Enter interest to search for:')
interest = input()

interst = interest.lower()

for x in feed.entries:
    event_title = x.title
    event_title=event_title.lower()
    if(interest in event_title):
        print('Event found with interest:')
        print(x.title)
        if(x.description != x.title):
            print(x.description)
        print(x.event_begindatetime)
