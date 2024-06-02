from setuptools import setup, find_packages


# Open the README file and read its contents
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# The version of the package
__version__ = "0.0.0"

# The name of the repository
REPO_NAME = "Bank-Chrun-Prediction"
# The username of the author
AUTHOR_USER_NAME = "amrahmed95"
# The name of the source code repository
SRC_REPO = "BankChurn"
# The email of the author
AUTHOR_EMAIL = "amr.ahmedm95@gmail.com"


def get_requirements(file_path: str) -> list[str]:
    """
    Reads the requirements from the file and returns a list of requirements.

    Args:
        file_path (str): The path to the requirements file.

    Returns:
        list[str]: A list of requirements.
    """
    # Open the file and read its contents
    with open(file_path) as f:
        # Read the requirements and remove the newline character
        requirements = [req.replace("\n", "") for req in f.readlines()]

        # If the entry is "-e .", remove it
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


# Setup the package with the given information
setup(
    # The name of the package
    name=SRC_REPO,
    # The version of the package
    version=__version__,
    # The author of the package
    author=AUTHOR_USER_NAME,
    # The email of the author
    author_email=AUTHOR_EMAIL,
    # A short description of the package
    description="End-to-End: customer churn prediction in banking",
    # The long description of the package
    long_description=long_description,
    # The URL of the repository
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    # The project URLs
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    # The packages included in the package
    packages=find_packages(),
    # Include package data
    include_package_data=True,
    # Not zip safe
    zip_safe=False,
    # The requirements of the package
    install_requires=get_requirements('requirements.txt')
)
