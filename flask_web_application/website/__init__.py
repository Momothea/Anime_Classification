from flask import Flask
import logging
from prometheus_flask_exporter import PrometheusMetrics

def create_app():

    logging.basicConfig(level=logging.INFO)
    logging.info("Setting LOGLEVEL to INFO")

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bla bla bla'
    #metrics = PrometheusMetrics(app)
    #metrics.info("app_info", "App Info, ", version="1.0.0")
    

    from .views import views
    from .auth import auth

    app.static_folder = 'static'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app