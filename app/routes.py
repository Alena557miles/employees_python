from flask import request
from flask import render_template
from app import app
from app.models.employee import Employee

# Route handler for displaying the list of employees
@app.route('/')
def index():
    department_name = request.args.get('department', default=None, type=str)
    employees = Employee.load_employees()
    if department_name:
        employees = Employee.get_employees_by_department(department_name)
    return render_template('index.html', employees=employees)

# Route handler for displaying the detailed information of an employee
@app.route('/employee/<employee_id>')
def employee_detail(employee_id):
    employee = Employee.get_employee_by_id(employee_id)
    return render_template('detail.html', employee=employee)