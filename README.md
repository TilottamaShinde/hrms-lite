# HRMS Lite 🏢

A simple **Human Resource Management System (HRMS)** built in **Python** to demonstrate core HR features like employee management, attendance, leaves, and payroll.  
This is a **lite version**, perfect for learning, showcasing skills, and GitHub portfolio projects.  

---

## ✨ Features
- **Employee Management** 👩‍💼 – Add, view, delete employees  
- **Attendance Management** 🕒 – Mark and view attendance records  
- **Leave Management** 🌴 – Apply, view, approve/reject leaves  
- **Payroll Management** 💰 – Generate and view employee payslips  

---

## 📂 Project Structure

HRMS_Lite/

│── main.py # Entry point with menu

│── utils.py # Database helpers (load/save)

│── employees.py # Employee management

│── attendance.py # Attendance management

│── leaves.py # Leave management

│── payroll.py # Payroll management

│── db.json # JSON file acting as database

│── README.md # Project documentation

##  Setup & Run
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/HRMS_Lite.git
   cd HRMS_Lite

Run
python main.py


## Database

Data is stored in a local file db.json (acts as a database).


## Future Enhancements

User authentication (Admin/Employee login)

GUI with Tkinter or Flask Web App

Report generation (PDF/Excel)

Integration with SQL database
