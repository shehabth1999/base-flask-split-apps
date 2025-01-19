# Base Flask Splited Apps

This is a modular Flask application designed to be scalable and easy to extend. It includes built-in CLI commands for creating new app modules and follows Flask's best practices for configuration and app organization.

---

## Features

- Modular structure for building multiple app modules.
- Easy creation of new app modules using the `flask create-app` CLI command.
- Integration-ready with extensions like SQLAlchemy and Flask-Migrate.
- Customizable configuration with support for Flask's default configuration pattern.
- Blueprints for routing and modularity.

---

## Requirements

- Python 3.8 or higher
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Any additional dependencies specified in `requirements.txt`

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-flask-app.git
   cd your-flask-app
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   Create a `.env` file and configure environment variables as needed:
   ```bash
   FLASK_APP=app.py
   FLASK_ENV=development
   ```

5. **Run the Application**
   ```bash
   flask run
   ```

---

## Usage

### Create a New App Module
To create a new app module, use the custom CLI command:
```bash
flask create-app <app_name>
```
This will generate a new app folder in the `apps` directory with the following structure:
```
apps/<app_name>/
    ├── __init__.py
    ├── models.py
    ├── routes.py
```

Example:
```bash
flask create-app blog
```

### Migrations
1. Initialize the database migration repository:
   ```bash
   flask db init
   ```

2. Create a migration:
   ```bash
   flask db migrate -m "Initial migration"
   ```

3. Apply the migration:
   ```bash
   flask db upgrade
   ```

---

## App Structure

```
project/
├── apps/
│   ├── <app_name>/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
├── migrations/
├── config.py
├── extensions.py
├── wsgi.py
├── requirements.txt
├── README.md
```

---

## Configuration

To customize the app configuration, modify `config.py`. Example:
```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
```

---

## Development Workflow

1. Start the development server:
   ```bash
   flask run
   ```

2. Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

3. Use the Flask CLI for tasks like creating new modules or running migrations.

---

## Future Improvements

- Add tests for the application.
- Add more CLI commands for tasks like managing users, seeding data, etc.
- Implement role-based access control.
- Integrate with a front-end framework like React or Vue.js.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
