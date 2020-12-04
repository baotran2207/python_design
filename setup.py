from setuptools import setup, find_packages

__version__ = "0.1"

setup(
    name="baoapi",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-sqlalchemy",
        "flask-restful",
        "flask-migrate",
        "flask-jwt-extended",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "python-dotenv",
        "passlib",
        "apispec[yaml]",
        "apispec-webframeworks",
    ],
    entry_points={
        "console_scripts": [
            "baoapi = baoapi.manage:cli"
        ]
    },
)
