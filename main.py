from twilio.rest import Client
import run
import urllib
import feedparser

print(run.toReturn)

#contents = urllib.request.urlopen("http://ruevents.rutgers.edu/events/getEventsRss.xml?numberOfDays=7").read()
#feed = feedparser.parse('http://ruevents.rutgers.edu/events/getEventsRss.xml?numberOfDays=7')

account_sid = 'ACc58f8372eb9b75f8d5fe4d587bccd167'
auth_token = '54ed90c4225c224e23f0d35568b307d8'

client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               from_='+12055129674',
#                               body='Welcome to RUHelp',
#                               to='+17326667804'
#                           )

def noDupeInsert(arr, x):
    insert = True
    for (y in arr):
        if (y==x):
            insert= False

    return insert

def EventLogic(ar):
    #changing title to lowercase if
    if (ar[2]!='-'):
        ar[2]=ar[2].lower()
     
    toReturn =[]
    for (x in feed.entries):
        if (ar[0]==x.date & ar[0]!='-'):
            #code
            #need to check if the array already contains the event
            if (noDupeInsert(toReturn,x)):
                toReturn.append(x)
        elif (ar[1]==x.time & ar[1]!='-'):
            #code
            if (noDupeInsert(toReturn,x)):
                toReturn.append(x)
        elif (ar[2] in x.event.lower() & ar[2]!='-'):
            #code
            if (noDupeInsert(toReturn,x)):
                toReturn.append(x)
    return toReturn

#for returning texts to bot will need to check if all 3 args are - or not
def textLogic(arr):
    if (arr[0]=='-' && arr[1]=='-' && arr[2]=='-'):
       #code for if user does not specify input keywords (date, time, title) 
       #we need to send texts here 
    else :
        #code for if user has specified input keywords
        toUse = EventLogic(arr)
        #we need to send texts here
    

        

def processing(x):
    #x is a string
    x=x.lower()
    x=x.split(' ')
    #now we have tokens seperated in spaces
    return x



print(message.sid)
print(contents)
print(str(len(feed['entries'])) + " events happening this week.")

for x in feed.entries:
     print (x.title)

print('Enter interest to search for:')
interest = input()

interest = interest.lower()
count = 0
for x in feed.entries:
    event_title = x.title
    event_title=event_title.lower()
    if(interest in event_title):
        count=count+1
        if(count > 5):
            break
        print("------------------------------")
         print('Event found with interest:')
        print(str(count)+'. ', end = '')
        title = str(x.title)
        print(title[0:20]+'...')
         print(x.title)
         if(x.description != x.title):
             print(x.description)
         print(x.event_begindatetime)

print("Please enter the number of any event that interests you, or send 0 to cancel")
eventNum = input()
