from flask import Flask
import requests
from flask_cors import CORS




def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SECRET_KEY'] = 'secret-key'


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
      


    return app