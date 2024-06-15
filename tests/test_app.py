import unittest
from flask import Flask, render_template
from app.models.employee import Employee

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__, template_folder='../app/templates')
        self.app.config['TESTING'] = True

    def tearDown(self):
        pass

    def test_employee_detail(self):
        with self.app.test_request_context('/employee/1'):
            employee = Employee('John', 'Doe', 5, 'Software Development', 'Main Responsibilities', 'Department')
            rendered_template = render_template('detail.html', employee=employee)
            self.assertIn('John', rendered_template)
            self.assertIn('Doe', rendered_template)
            self.assertIn('5', rendered_template)
            self.assertIn('Software Development', rendered_template)

if __name__ == '__main__':
    unittest.main()