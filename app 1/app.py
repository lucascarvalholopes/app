from flask import Flask
from routes import setup_routes
from database import init_db

app = Flask(__name__)

# Setup database
init_db(app)

# Setup routes
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True)