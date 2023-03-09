from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bla bla bla'
    #metrics = PrometheusMetrics(app)
    #metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")
    

    from .views import views
    from .auth import auth

    app.static_folder = 'static'
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app