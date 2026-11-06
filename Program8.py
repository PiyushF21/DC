import csv

clients=[]

with open("cristian_clocks_8.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        clients.append(row)

for client in clients:
    id = client["client_id"]
    T0 = float(client["t0_send_ms"])
    Tserver = float(client["t_server_ms"])
    T1 = float(client["t1_recv_ms"])
    Rtt = T1-T0
    Testimated = Tserver + (Rtt//2)
    adjustments = Testimated-T1
    print("Adjustment for " ,id , adjustments)