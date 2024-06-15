# My Web App

This is a web application built with Python using the Flask framework. It displays a list of employees and provides detailed information about each employee.

## Project Structure

The project has the following file structure:

```
my-web-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   ├── index.html
│   │   └── detail.html
│   └── models
│       └── employee.py
├── tests
│   └── test_app.py
├── run.py
├── config.py
└── README.md
```

## Files

- `app/__init__.py`: This file initializes the Flask application and sets up the database connection.

- `app/routes.py`: This file contains the route handlers for the application. It defines two routes: `/` for displaying the list of employees and `/employee/<employee_id>` for displaying the detailed information of a specific employee.

- `app/templates/index.html`: This HTML template file displays the list of employees. It uses Jinja2 templating to dynamically render the employee names and surnames.

- `app/templates/detail.html`: This HTML template file displays the detailed information of an employee. It receives the employee's name, surname, years of experience, and main responsibilities as parameters.

- `app/models/employee.py`: This file defines the `Employee` class, which represents an employee. It has properties for name, surname, years of experience, and main responsibilities.

- `tests/test_app.py`: This file contains unit tests for the application.

- `run.py`: This file is the entry point of the application. It creates an instance of the Flask app and runs it.

- `config.py`: This file contains configuration settings for the application, such as the database connection details.

## Usage

To run the application, execute the following command:

```
python run.py
```

Open your web browser and navigate to `http://localhost:5000` to view the list of employees.

## Testing

To run the unit tests for the application, execute the following command:

```
python -m unittest discover tests
```

## Dependencies

The project requires the following dependencies:

- Flask
- Jinja2

You can install the dependencies by running the following command:

```
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.