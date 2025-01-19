import os
import click  # Flask CLI uses Click for argument handling


class AppCreator:
    def __init__(self, apps_dir):
        self.apps_dir = apps_dir

    def create_app(self, app_name):
        """Create a new Flask app module."""
        # Define the app directory path
        app_dir = os.path.join(self.apps_dir, app_name)

        # Check if the app folder already exists
        if os.path.exists(app_dir):
            print(f"Error: The folder '{app_name}' already exists in {self.apps_dir}.")
            return  # Exit without raising an error

        # Create the app folder
        os.makedirs(app_dir, exist_ok=True)

        # Create __init__.py file
        init_file = os.path.join(app_dir, '__init__.py')
        with open(init_file, 'w') as f:
            f.write("from flask import Blueprint\n")
            f.write(f"app = Blueprint('{app_name}', __name__)\n")
            f.write("from . import routes, models\n")

        # Create models.py file
        models_file = os.path.join(app_dir, 'models.py')
        with open(models_file, 'w') as f:
            f.write(f"# Models for {app_name}\n")
            f.write("from extensions import db\n")

        # Create routes.py file
        routes_file = os.path.join(app_dir, 'routes.py')
        with open(routes_file, 'w') as f:
            f.write(f"# Routes for {app_name}\n")
            f.write("from . import app\n")

        print(f"App '{app_name}' created successfully!")

    def init_app(self, app):
        """Register Flask CLI commands."""
        @app.cli.command("create-app")
        @click.argument("app_name")  # Use Click to handle the `app_name` argument
        def create_app_cli(app_name):
            """Create a new Flask app module."""
            # Call the `create_app` method with the provided app name
            self.create_app(app_name)
