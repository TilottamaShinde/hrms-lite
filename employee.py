import uuid
from uuid import uuid4

from utils import load_db, save_db

def add_employee(name, department, role, salary):
    db = load_db()

    employee = {
        "id" : str(uuid.uuid4()),
        "name":name,
        "department":department,
        "role":role,
        "salary":salary
    }
    db["employees"].append(employee)
    save_db(db)
    print(f"Employee {name} added successfully")

def view_employees():
    db = load_db()
    employees = db.get("employees",[])
    if not employees:
        print("No employee found")
    else:
        print("\n---Employee List---")
        for emp in employees:
            print(f"ID:{emp['id']} | Name {emp['name']} | Dept {emp['department']} Role {emp['role']} | Salary {emp['salary']}")

def delete_employee(emp_id):
    db = load_db()
    employees = db.get("employees",[])
    updated_list = [emp for emp in employees if emp["id"]!=emp_id]

    if len(employees) == len(updated_list):
        print("Employee not found!")
    else:
        db["employees"] = updated_list
        save_db(db)
        print(f"Employee with id {emp_id} deleted successfully!")