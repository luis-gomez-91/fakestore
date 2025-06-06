from flask import Flask
from app.routes.login import login_bp
from app.routes.products import products_bp
from app.routes.logout import logout_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'mi_clave_secreta' 

    app.register_blueprint(login_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(logout_bp)

    return app