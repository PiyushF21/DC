import csv
def processData(value):
    return 2*value
with open("rpc_calls_1.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        call_id = row["call_id"]
        client = row["client_name"]
        method = row["method_name"]
        value = int(row["param_value"])
        print("\n[Dispatch]")
        print(client , " invoking " , method)
        request = [method,value]
        print("Marshalled Request " , request)
        print("Processing parameter")
        if method == "processData":
            print(processData(value))
        else:
            print("Invalid method")