# This file contains the main views or endpoint of the application.
from flask import Blueprint, render_template, request
from prometheus_client import start_http_server, Summary, Counter, Info
#i = Info('app_info', 'Application info', version='1.0.3')
#c = Counter('http_requests_total', 'HTTP Requests total', labels=['GET', '/'])

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/classify', methods=['GET','POST'])
def classify():
    #data = request.form
    #print(data) # print an ImmutableMultiDict
    if request.method == 'POST':
        Title = request.form.get('Title')
        Genre = request.form.get('Genre')
        Description = request.form.get('Description')
        Producer = request.form.get('Producer')
        Studio = request.form.get('Studio')
        title = request.form.get('title')
        return render_template("classify.html", title =  Title)

    return render_template("classify.html")