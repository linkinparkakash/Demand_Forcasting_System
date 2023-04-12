from setuptools import setup

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

SRC_REPO = "src"
AUTHOR_NAME = "linkinparkakash"
REPO_NAME = "Demand_Forcasting_System"
LIST_OF_REQUIREMENTS = []

setup(name=SRC_REPO,
      version="0.0.1",
      author=AUTHOR_NAME,
      description='This is our first release',
      long_description=long_description,
      url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
      author_email="datasciencenini@hotmail.com",
      packages=SRC_REPO,
      python_requires=">=3.10",
      install_requires=LIST_OF_REQUIREMENTS)

