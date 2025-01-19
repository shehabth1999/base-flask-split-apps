from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from scripts.add_new_app import AppCreator
import config



db = SQLAlchemy()  # Initialize the SQLAlchemy object
migrate = Migrate()  # Initialize the Migrate object "" CLI ""
app_creator = AppCreator(config.APPS_DIR)  # Initialize the AppCreator object "" CLI ""