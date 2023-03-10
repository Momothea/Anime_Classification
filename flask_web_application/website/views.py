# This file contains the main views or endpoint of the application.
from flask import Blueprint, render_template, request, Response, json
import prometheus_client
import time
import requests
from prometheus_client import start_http_server, Summary, Counter, Info, Histogram
#from prometheus_client.core import CollectorRegistry
import random

views = Blueprint('views', __name__)

_INF = float("inf")

graphs = {}


graphs['c'] = Counter('python_request_operations_total','the total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds', buckets=(1,2, 5, 10, _INF))

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/classify', methods=['GET','POST'])
def classify():
    #graphs['c'].inc()
    #data = request.form
    #print(data) # print an ImmutableMultiDict
    if request.method == 'POST':
        Title = request.form.get('Title')
        Genre = request.form.get('Genre')
        Description = request.form.get('Description')
        Producer = request.form.get('Producer')
        Studio = request.form.get('Studio')
        Type = request.form.get('Type')

        data = {'Title':Title,
                'Genre':Genre,
                  'Description':Description,
                  'Producer':Producer,
                  'Studio':Studio,
                  'Type': Type}
        
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}

        

        response = requests.post('http://model:5001/receive_data', json=json_data, headers=headers)

        data = response.text

        return render_template("classify.html", title =  str(data))

    return render_template("classify.html")

@views.route('/metrics')
def request_count():

    res = []
    print("Hello world")
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    
    return Response(res, mimetype='text/plain')
#    return ({"message": "hello"}) 
