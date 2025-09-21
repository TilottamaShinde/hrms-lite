from utils import init_db

def main():
    init_db()
    while True:
        print("\n=== HRMS Lite===\n")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee ")
        print("4. Mark Attendance")
        print("5. View Attendance  ")
        print("6. Apply Leave")
        print("7. View Leaves")
        print("8. Approve/Reject Leave ")
        print("9. Generate Payslip")
        print("10. View Payroll")
        print("0. Exit")

        choice = input("Enter your choice : ")
        if choice == "0":
            print("Exiting.... Bye...")
            break
        else:
            print("Feature not yet implemented.")

if __name__ == "__main__":
    main()
