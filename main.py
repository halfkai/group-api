from flask import Flask
from app import create_app

if __name__ == '__main__':
    app = create_app()
    Flask.run(
        app,
        debug=True,
        port=60000,
    )
