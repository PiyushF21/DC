import csv 

nodes=[]
with open("ring_nodes_15.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        nodes.append(row)

active=[]

for node in nodes:
    if node["is_active"].upper()=="TRUE":
        active.append(int(node["node_id"]))

initiator = min(active)
current = initiator
participants=[]

while True:
    print("Token reached " , current)
    participants.append(current)

    for node in nodes:
        if int(node["node_id"])==current:
            next_id = int(node["next_node_id"])
            break

    while next_id not in active:
        print("Skipping node " , next_id)
        for node in nodes:
           if int(node["node_id"])==next_id:
                next_id = int(node["next_node_id"])
                break

    current = next_id
    if current==initiator:
        break

leader = max(participants)
print(leader)

            
        
