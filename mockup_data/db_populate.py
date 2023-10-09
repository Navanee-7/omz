import pandas as pd
import requests 
import csv
from datetime import datetime

def post_accesspoints():
    
    #Pre-processing
    #preprocess_ap()
    
    accesspoints_file_path = "csv_files/AccessPoints.csv"
    ap_data = pd.read_csv(accesspoints_file_path)
    ap_url = "http://127.0.0.1:8000/api/v1/accesspoints/"

    #Populating the AccessPoints table
    ap_json_data = []
    with open(accesspoints_file_path,'r') as ap_file: 
        ap_reader = csv.DictReader(ap_file)
        for row in ap_reader:
            response = requests.post(ap_url, json=row)
            if response.status_code == 201:
                print("AccessPoints successfully populated")
                print('Response:', response.json())
            else: 
                print("Failed to populate AccessPoints")
                print('Response:', response.text)
            ap_json_data.append(row)
    print(ap_json_data)
    
    #POSTing the AccessPoints to the API
    # for item in ap_json_data:
    #     response = requests.post(ap_url, json=item)
    #     if response.status_code == 200:
    #         print("AccessPoints successfully populated")
    #         print('Response:', response.json())
    #     else: 
    #         print("Failed to populate AccessPoints")
    #         print('Response:', response.text)
    
def post_sites():
    sites_file_path = "csv_files/Sites.csv"
    sites_data = pd.read_csv(sites_file_path)
    sites_url = "http://127.0.0.1:8000/api/v1/sites/"
        
    #Populating the Sites table
    sites_json_data = []
    with open(sites_file_path,'r') as sites_file:
        sites_reader = csv.DictReader(sites_file)
        for row in sites_reader:
            
            response = requests.post(sites_url, json=row)
            if response.status_code == 200:
                print("Sites successfully populated")
                print('Response:', response.json())
            else: 
                print("Failed to populate Sites")
                print('Response:', response.text)
            sites_json_data.append(row)
    #print(sites_json_data[0])
          
    #POSTing the Sites to the API
    # for item in sites_json_data:
    #     response = requests.post(sites_url, json=item)
    #     if response.status_code == 200:
    #         print("Sites successfully populated")
    #         print('Response:', response.json())
    #     else: 
    #         print("Failed to populate Sites")
    #         print('Response:', response.text)

def preprocess_ap():
    ap_data = pd.read_csv("csv_files/AccessPoints.csv")
    ap_data['Activated'] = ap_data['Activated'].str[:10]
    ap_data['Activated'] = pd.to_datetime(ap_data['Activated'],errors="coerce")
    ap_data.to_csv("csv_files/AccessPoints.csv", index=False)
    
def populate_db():
    preprocess_ap()
    post_accesspoints()
    # post_sites()
    
#Main
def main():
    populate_db()
    
if __name__ == "__main__":
    main()