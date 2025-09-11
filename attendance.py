from utils import load_db,save_db
from datetime import datetime

def mark_attendance(emp_id, status):
    """
    mark attendance for employees
    status = 'Present' or 'Absent'
    :param emp_id:
    :param status:
    :return:
    """
    db = load_db()

    #Check if employee exist
    employees =  db.get('employees',[])
    if not any(emp["id"] == emp_id for emp in employees):
        print("Employee not found")
        return

    attendance = db.get("attendance",[])

    record = {
        "emp_id":emp_id,
        "date":datetime.now().strftime("%Y-%m-%d"),
        "status":status
    }
    attendance.append(record)
    db["attendance"] = attendance
    save_db(db)
    print(f"Attendance marked for employee {emp_id} as {status}")

def view_attendance(emp_id=None):
    """
    View attendance for all or specific employee
    :param emp_id:
    :return:
    """
    db = load_db()
    attendance = db.get("attendance",[])

    if not attendance:
        print("No attendance record found!")
        return
    print("\n---Attendance Records---\n")
    for record in attendance:
        if emp_id is None or record["emp_id"] == emp_id:
            print(f"EmpId :{record['emp_id']} | Date : {record['date']} | Status : {record['status']}")
