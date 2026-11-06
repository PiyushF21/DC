import csv 
nodes=[]

with open("node_clocks_3.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        nodes.append(row)

working_nodes_clock = []
for node in nodes:
    print(node["node_id"],"->" , node["clock_time_sec"])
    if node["is_faulty"].upper()=="FALSE":
        working_nodes_clock.append(int(node["clock_time_sec"]))

average = sum(working_nodes_clock)/len(working_nodes_clock)

for node in nodes:
    if node["is_faulty"].upper()=="FALSE":
        print("adjustments " , average-int(node["clock_time_sec"]))

                                   