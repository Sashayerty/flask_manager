import argparse
import os

config_file_inner = """class Config:

    DEBUG = True


config = Config()
"""


parser = argparse.ArgumentParser(
    prog="flask_manager",
    usage="%(prog)s [args] [project_name]",
    description="Simple CLI program to create base "
    "structure of Flask application.",
)
parser.add_argument(
    "--project-name",
    "-p",
    type=str,
    required=True,
    metavar="Name of project",
)
project_name: str = parser.parse_args().project_name
run_file_inner = f"""from {project_name} import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
"""
init_file_inner = f"""from {project_name}.config import config
from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    return app
"""
if len(project_name.split()) > 1:
    project_name = "_".join(project_name.split())

a = input("Do you wanna to create app [y/N]? ")
name_of_app = False
if a == "y":
    while not name_of_app:
        name_of_app = input("Write name of first app: ")
        if not name_of_app:
            print("Name of app must be not empty string!")
            continue
try:
    os.mkdir(path=f"./{project_name}")
    run_file = open(f"./{project_name}/run.py", "w")
    run_file.write(run_file_inner)
    os.mkdir(path=f"./{project_name}/{project_name}")
    os.mkdir(f"./{project_name}/{project_name}/templates")
    os.mkdir(f"./{project_name}/{project_name}/static")
    if name_of_app:
        routes_file_inner = f"""from flask import Blueprint

{name_of_app} = Blueprint(
    '{name_of_app}',
    __name__,
    template_folder="../templates/{name_of_app}",
)


@{name_of_app}.route("/", methods=["POST", "GET"])
def index():
    return 'Hello, world!'
"""
        os.mkdir(f"./{project_name}/{project_name}/{name_of_app}")
        os.mkdir(f"./{project_name}/{project_name}/templates/{name_of_app}")
        routes_file = open(
            f"./{project_name}/{project_name}/{name_of_app}/routes.py", "w"
        )
        routes_file.write(routes_file_inner)
        init_file_inner = f"""from app.config import config
from flask import Flask

from {project_name}.{name_of_app}.routes import {name_of_app}


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint({name_of_app})
    return app
        """
    init_file = open(f"./{project_name}/{project_name}/__init__.py", "w")
    init_file.write(init_file_inner)
    config_file = open(f"./{project_name}/{project_name}/config.py", "w")
    config_file.write(config_file_inner)
    requirements_file = open(f"./{project_name}/requirements.txt", "w")
    requirements_file.write("flask")
    readme_file = open(f"./{project_name}/README.md", "w")
    print(f"Project {project_name} created successfully!")
except Exception as e:
    print(e)
