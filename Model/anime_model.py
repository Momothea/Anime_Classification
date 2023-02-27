from flask import Flask, request, json
import time
from prometheus_client import start_http_server, Summary, Counter, Info, Histogram
from prometheus_client.core import CollectorRegistry
from prometheus_flask_exporter import PrometheusMetrics



_INF = float("inf")

app = Flask(__name__)

PrometheusMetrics(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/receive_data', methods=['POST'])
def receive_data():
    json_data = request.get_json()
    data = json.loads(json_data)
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port = 5001)
