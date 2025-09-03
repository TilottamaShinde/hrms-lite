from utils import init_db

def main():
    init_db()
    while True:
        
        print("\n===HRMS Lite===\n")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Delete Employee")
        print("4. Exit")
       """ print("1. Employee Management")
        print("2. Attendance")
        print("3. Leave Management")
        print("4. Payroll")
        print("5. Reports ")
        print("0. Exit")"""

        choice = input("Enter your choice : ")
        if choice == "0":
            print("Exiting.... Bye...")
            break
        else:
            print("Feature not yet implemented.")

if __name__ == "__main__":
    main()
