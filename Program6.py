import csv
events =[]
with open("vector_event_6.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
         events.append(row)

vectors =[]
clocks=[[0,0,0],[0,0,0],[0,0,0]]
messages = [[0,0,0],[0,0,0],[0,0,0]]

for event in events:
    p = int(event["event_id"][1])-1
    target = event["target_process"]
    if event["event_action"]=="SEND":
        clocks[p][p]+=1
        reciever = int(target[1])-1
        messages[reciever]=clocks[p].copy()
        print(event["event_id"], "SEND:", clocks[p])
    elif event["event_action"]=="RECIEVE":
        sender = int(target[1])-1
        for i in range(3):
            clocks[p][i]=max(clocks[p][i],messages[p][i])
        clocks[p][p]+=1
        print(event["event_id"], "RECEIVE:", clocks[p])
    else:
        clocks[p][p]+=1
        print(event["event_id"], "LOCAL:", clocks[p])
    vectors.append(clocks[p].copy())

for i in range(len(vectors)):
    for j in range(i+1,len(vectors)):
        before = True
        after = True
        for k in range(3):
            if vectors[i][k]>vectors[j][k]:
                before = False
            if vectors[i][k]<vectors[j][k]:
                after = False
        if before and not after:
            print(events[i]["event_id"], "happened before", events[j]["event_id"])
        elif after and not before:
            print(events[j]["event_id"], "happened before", events[i]["event_id"])
        else:
            print(events[i]["event_id"], "and", events[j]["event_id"], "are CONCURRENT")
