from flask import Flask
from sqlalchemy import create_engine
from flask_cors import CORS
from models import Base

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])

# Database setup
engine = create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)

from position import position_routes
from command import command_routes

app.register_blueprint(position_routes.position_routes)
app.register_blueprint(command_routes.command_routes)

if __name__ == '__main__':
    app.run(debug=True)
