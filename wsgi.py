from flask import Flask
import config
import importlib
from extensions import db, migrate, app_creator


class Application:
    def configure_extensions(self, app:Flask):
        db.init_app(app)
        migrate.init_app(app, db)
        app_creator.init_app(app)

    def configure_installed_apps(self, app:Flask):
        # Dynamically import and register blueprints from INSTALLED_APPS
        for app_module in config.INSTALLED_APPS:
            try:
                module = importlib.import_module(f'{config.APPS_DIR}.{app_module}')
                app.register_blueprint(module.app, url_prefix=f"/{app_module}/")
            except Exception as e:
                print(f"Error importing or registering app {app_module}: {e}")

    def create_app(self):
        app = Flask(__name__)
        app.config.from_object(config.Config)
        self.configure_installed_apps(app)
        self.configure_extensions(app)
        return app

def create_app():
    return Application().create_app()

if __name__ == "__main__":
    app = create_app()  # Create app using the factory function
    app.run()  # Run the app directly