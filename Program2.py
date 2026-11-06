import csv
nodes = []
with open("bully_cluster_2.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        nodes.append(row)
alive = []
for node in nodes:
    if node["is_alive"].upper()=="TRUE":
        alive.append(int(node["node_id"]))
for node in nodes:
    if node["is_current_coordinator"].upper()=="TRUE":
        print("Node " ,node["node_id"] , " Failed")
        break
initiator = min(alive) 
current = initiator
while True:
    higher_nodes =[]
    for node in nodes:
        if int(node["node_id"])>current:
            higher_nodes.append(int(node["node_id"]))
    if len(higher_nodes)==0:
        print(current , " is the new co ordinator")
        break
    for node_id in higher_nodes:
        print("[ELECTION] Node", current, "sends ELECTION to Node", node_id)
        print("[OK] Node", node_id, "responds to Node", current)
    current = max(higher_nodes)