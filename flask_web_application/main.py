from website import create_app
from prometheus_flask_exporter import PrometheusMetrics


app = create_app()

metrics = PrometheusMetrics(app = app)
metrics.info("app_info", 'Application info', version='1.0.3')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0") #debug true since we are in development. Put 'off' in production