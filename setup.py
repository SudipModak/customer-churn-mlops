from setuptools import setup,find_packages

setup(
    name="customer_churn",
    version="0.0.1",
    author="Sudip Modak",


    author_email="SudipModak719@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"":"src"},

)