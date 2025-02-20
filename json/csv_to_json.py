import csv 
import json

def csc_json(csv_o, json_y):
    with open(csv_o, "r") as file:
        csv_data=csv.DictReader(file)
        
        json_data=json.dumps(list(csv_data, indent=4))
        
        
        with open(json_y, "w") as json_y:
            json_y.write(json_data)
            
            

csv_o = "vhy.csv"
json_y = "jhu.json"


csc_json(vhy.csv, jhu.json)
