import os

# Applications directory that hold apps.
APPS_DIR = 'apps'

# List of apps that are installed in the application. Each app should have a file named 'routes.py' in its directory.
""" Use command       -------->          flask create-app <app_name>        <----------       to auto create app """
INSTALLED_APPS = [
    'accounts'
]

# Configuration for Flask application
class Config:
    # make sure that the secret key is secure in production
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dklfhsdj23%13!faf~gdsg$%<>JL<edsgdsfadfafdaFA&@!SFawrq24k45fFwf!wo12uj4iphjt')
    
    # Set the path for the SQLite database file in the same directory as this script
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Get the directory of the current script
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'sqlite.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False