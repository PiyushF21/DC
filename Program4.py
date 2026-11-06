import csv 
import threading
import time

tasks =[]
with open("tasks_4.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        tasks.append(row)

completed = []
lock = threading.Lock()

def process_task(task):
    print(task["thread_name"] , " Processing " , task["task_id"])
    time.sleep(int(task["burst_ms"])/1000)
    lock.acquire()
    print(task["thread_name"] , "Acquired lock")
    completed.append(task["task_id"])
    print(task["thread_name"] , "Released lock")
    lock.release()

threads =[]
for task in tasks:
    t= threading.Thread(target=process_task,args=(task,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(completed)