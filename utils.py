import json
import os

DB_FILE = "db.json"
def init_db():
    """create a new database file if it does not exist"""
    if not os.path.exists(DB_FILE):
        data = {
            "employees":[],
            "attendance":[],
            "leaves":[],
            "payroll":[]
        }
        save_db(data)

def load_db():
    """load data from json file"""
    with open(DB_FILE,"r") as f:
        return json.load(f)

def save_db(data):
    """save data to json file"""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent = 4)
