import csv

events=[]
with open("events_7.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        events.append(row)

clocks =[0,0,0]
messages = [0,0,0]

for event in events:
    p = int(event["process_id"][1])-1
    target = event["message_to"]
    if event["event_type"]=="SEND":
        clocks[p]+=1
        reciever = int(target[1])-1
        messages[reciever]=clocks[p]
    elif event["event_type"] == "RECEIVE":
        clocks[p] = max(clocks[p], messages[p]) + 1
    else:
        clocks[p]+=1
    event["timestamp"]=clocks[p]

events.sort(key=lambda x:(int(x["timestamp"]),x["process_id"]))

for event in events:
    print(event["event_id"], "Timestamp:", event["timestamp"])