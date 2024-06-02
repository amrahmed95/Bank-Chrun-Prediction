import os
import sys
import logging
from pathlib import Path


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)


def create_file_structure(project_name):
    """
    Create file structure for the given project name.

    Args:
        project_name (str): Name of the project.
    """
    # List of files to be created in the project
    list_of_files = [
        ".github/workflows/.gitkeep",
        f"src/{project_name}/__init__.py",
        f"src/{project_name}/components/__init__.py",
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/utils/common.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/entity/config_entity.py",
        f"src/{project_name}/constants/__init__.py",
        "config/config.yaml",
        "params.yaml",
        "schema.yaml",
        "main.py",
        "app.py",
        "Dockerfile",
        "requirements.txt",
        "setup.py",
        "research/trials.ipynb",
        "templates/index.html",
    ]

    # Create directories and files
    for file_path in list_of_files:
        file_path = Path(file_path)
        filedir, filename = os.path.split(str(file_path))

        # Create directories
        if filedir != "":
            os.makedirs(Path(filedir), exist_ok=True)
            logging.info(f"Creating Directory: {filedir} for the file {filename}")

        # Create files
        if (not os.path.exists(str(file_path))) or (os.path.getsize(str(file_path)) == 0):
            with open(str(file_path), "w") as f:
                pass
                logging.info(f"Creating empty file: {file_path}")
                
        else:
            logging.info(f"{file_path} already exists")


if __name__ == "__main__":
    # Create file structure for the given project name
    create_file_structure(project_name="BankChurn")


