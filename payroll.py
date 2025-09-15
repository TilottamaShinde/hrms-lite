from utils import load_db, save_db
from datetime import datetime

def generate_payslip(emp_id, month, year):
    db = load_db()
    employees = db.get("employees",[])

    employee = next((emp for emp in employees if emp["id"] == emp_id), None)
    if not employee:

        print("Employee not found!")
        return
    salary = employee.get("salary", 0)

    payslip = {
            "emp_id": emp_id,
            "name": employee["name"],
            "month": month,
            "year": year,
            "salary": salary,
            "generated_on": datetime.now.strftime("%Y-%m-%d")
    }

    db.setdefault("payroll",[]).append(payslip)
    save_db(db)
    print(f"Payslip generated for {employee['name']}({month}/{year}")

def view_payroll():
    db = load_db()
    payrolls = db.get("payroll",[])

    if not payrolls:
        print("No payroll records found.")
        return
    print("\n---Payroll Records ---")
    for p in payrolls:
        print(f"EmpID: {p['emp_id']} | Name: {p['name']} | {p['month']}/{p['year']} | "
              f"Salary: {p['salary']} | Generated on: {p['generated_on']}")