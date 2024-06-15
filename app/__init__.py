from flask import Flask

app = Flask(__name__)

# Database configuration
app.config['DATABASE'] = 'your_database_connection_string'

# Import routes
from app import routes