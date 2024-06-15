import json
import sqlite3
from typing import List, Optional

class Employee:
    employees: List['Employee'] = []

    def __init__(self, employee_id, name, surname, years_of_experience, main_responsibilities, department):
        self.employee_id = employee_id
        self.name = name
        self.surname = surname
        self.years_of_experience = years_of_experience
        self.main_responsibilities = main_responsibilities
        self.department = department
        Employee.employees.append(self)

    @staticmethod
    def get_employee_by_id(employee_id) -> Optional['Employee']:
        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM employees WHERE employee_id=?", (employee_id,))
        employee_data = c.fetchone()
        conn.close()

        if employee_data is None:
            return None

        employee = Employee(*employee_data)
        return employee
    
    @staticmethod
    def get_employees_by_department(department_name) -> List['Employee']:
        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM employees WHERE department=?", (department_name,))
        employees_data = c.fetchall()
        conn.close()

        employees = []
        for data in employees_data:
            employee = Employee(*data)
            employees.append(employee)
        
        return employees
    
    @staticmethod
    def load_employees():
        employees = []
        with open('employees.json', 'r') as f:
            employee_data = json.load(f)

        for data in employee_data:
            employee = Employee(data['employee_id'], data['name'], data['surname'], data['years_of_experience'], data['main_responsibilities'], data['department'])
            employees.append(employee)
        
        return employees
    
    @staticmethod
    def get_all_employees():
        conn = sqlite3.connect('employees.db')
        c = conn.cursor()
        c.execute("SELECT * FROM employees")
        employees_data = c.fetchall()
        conn.close()

        employees = []
        for data in employees_data:
            employee = Employee(*data)
            employees.append(employee)
        
        return employees

def create_table():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS employees
        (employee_id INTEGER PRIMARY KEY, name TEXT, surname TEXT, years_of_experience INTEGER, main_responsibilities TEXT, department TEXT)
    ''')

    conn.commit()
    conn.close()

def insert_employees():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()

    for employee in Employee.get_all_employees():
        c.execute('''
        INSERT OR IGNORE INTO employees (employee_id, name, surname, years_of_experience, main_responsibilities, department)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (employee.employee_id, employee.name, employee.surname, employee.years_of_experience, employee.main_responsibilities, employee.department))

    conn.commit()
    conn.close()

# Create table in the database
create_table()

# Insert employees into the database
insert_employees()

