from flask import Flask
from flask_cors import CORS
from find_a_friend.models.sqlite.settings.connection import db_connection_handler
from find_a_friend.main.routes.pets_routes import pet_route_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)
app.register_blueprint(pet_route_bp)


