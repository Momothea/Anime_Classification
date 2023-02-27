from flask import Flask, request, json

app = Flask(__name__)

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