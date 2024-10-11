from .main import main
from .auth import auth
from .admin import admin
from .test import test
from .data_register import data_register

def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(test)
    app.register_blueprint(data_register)
