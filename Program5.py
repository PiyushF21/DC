import csv 

jobs=[]

with open("workload_51.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        jobs.append(row)

workers = ["worker1","worker2","worker3"]
load=[0,0,0]

for i in range(len(jobs)):
    worker = i%3
    jobs[i]["assigned_worker"]=workers[worker]
    jobs[i]["status"]="Assigned"
    units = int(jobs[i]["compute_units"])
    load[worker]+=units
    print(jobs[i]["job_id"], "assigned to", workers[worker])
print(load)
for job in jobs:
    print(job["job_id"], job["assigned_worker"], job["status"])