# Flask Manager [![Generic badge](https://img.shields.io/badge/Crafted_with_Python_for-Flask-green.svg)](https://github.com/Sashayerty/flask_manager)

Flask Manager is a simple command-line interface (CLI) tool designed to help you quickly set up the base structure of a Flask application. This tool automates the creation of essential files and directories, allowing you to focus on developing your application rather than setting up the project structure.

## Features

- **Automatic Project Structure Creation**: Generates the necessary directories and files for a Flask application.
- **Automatic Git initialization**: Initializing git-repository.
- **Customizable Project Name**: Allows you to specify the name of your project.
- **Optional App Creation**: Provides an option to create an initial app within your project.
- **Blueprint Support**: Sets up a basic Blueprint for your app if you choose to create one.

## Installation

To use Flask Manager, you need to have Python installed on your system. You can clone the repository and run the script directly.

```bash
git clone https://github.com/Sashayerty/flask_manager --depth 1
cd ./flask_manager
```

## Usage

To create a new Flask project, run the following command:

```bash
python flask_manager.py --project-name <your-project-name>
```

Replace `<your-project-name>` with the desired name of your project.

### Example

```bash
python flask_manager.py --project-name my_flask_app
```

### Optional App Creation

After specifying the project name, you will be prompted to create an initial app. If you choose to do so, you will be asked to provide a name for the app.

```bash
Do you wanna to create app [y/N]? y
Write name of first app: my_app
```

## Building with PyInstaller (Cross-Platform)

To create a standalone executable for Windows, Linux, or macOS, follow these steps:

1. First install PyInstaller:

```bash
#Windows
pip install pyinstaller

#Linux/MacOS
pip3 install pyinstaller
```

2. Build the executable (platform-specific):

```bash
pyinstaller --onefile --name flask_manager flask_manager.py
```

This will create:

- Windows: dist/flask_manager.exe
- Linux/MacOS: dist/flask_manager

## Project Structure

The tool will create the following structure for your project:

```bash
my_flask_app/
│
├── my_flask_app/
│   ├── __init__.py
│   ├── config.py
│   ├── templates/
│   │   └── my_app/
│   ├── static/
│   └── my_app/
│       └── routes.py
│
├── .gitignore
├── run.py
├── requirements.txt
└── README.md
```

### Files and Directories

- **`.gitignore`**: Standard Python .gitignore
- **`run.py`**: Entry point for running the Flask application.
- **`requirements.txt`**: Contains the list of dependencies (initially includes `flask`).
- **`README.md`**: A basic README file for your project.
- **`my_flask_app/`**: Main directory for your Flask application.
  - **`__init__.py`**: Initializes the Flask app and registers Blueprints.
  - **`config.py`**: Configuration settings for the Flask app.
  - **`templates/`**: Directory for HTML templates.
  - **`static/`**: Directory for static files (CSS, JavaScript, images).
  - **`my_app/`**: Directory for the initial app (if created).
    - **`routes.py`**: Defines routes for the initial app using Blueprints.

## Configuration

The `config.py` file contains the configuration settings for your Flask application. You can modify this file to suit your needs.

```python
class Config:
    DEBUG = True

config = Config()
```

## Running the Application

To run your Flask application, navigate to the project directory and execute the following command:

```bash
python run.py
```

Your application will be accessible at `http://127.0.0.1:5000/`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
