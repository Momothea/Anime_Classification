from flask import Flask, request, json
import time
from prometheus_client import start_http_server, Summary, Counter, Info, Histogram
from prometheus_client.core import CollectorRegistry
from prometheus_flask_exporter import PrometheusMetrics
import joblib # Charger le modèle depuis le fichier
rf_loaded = joblib.load('random_forest_regressor.pkl')
import pandas as pd
import os
import random

print(os.listdir('/app/data/'))



# Synopsis 
import gensim
from sklearn.preprocessing import LabelEncoder # Charger un modèle Word2Vec pré-entraîné (par exemple GoogleNews-vectors-negative300)
w2v_model = gensim.models.KeyedVectors.load_word2vec_format(r'./GoogleNews-vectors-negative300-SLIM.bin.gz', binary=True)


def vectorize_sentence(sentence):
    vectors = []
    for word in sentence.split():
        if word in w2v_model:
            vectors.append(w2v_model[word])
    if len(vectors) > 0:
        return pd.DataFrame(vectors).mean().values
    else:
        return pd.Series([0]*300)
    
#vector_synopsis = vectorize_sentence(synopsis)
#final_synopsis = vector_synopsis.sum()
# Genre
#genre = genre.sort_values()# Encoder les variables catégorielles en variables numériques
#le = LabelEncoder()
#genre_float = le.fit_transform(genre)# Studio
#studio_float = le.fit_transform(studio)# Producer
#producer_float = le.fit_transform(producer)# Title
#title_float = le.fit_transform(title)
#type_float = le.fit_transform(Type)
#predictions = rf_loaded.predict([genre_float, final_synopsis, producer_float, studio_float, type_float, title_float] + [0]*25)





_INF = float("inf")

app = Flask(__name__)

PrometheusMetrics(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    data = json.loads(data)
    print(data,'lllllllllllllllllllllllllllllllllllllllllll')
    print(data['Title'])
    title = data['Title']
    genre = data['Genre']
    description = data['Description']
    producer = data['Producer']
    studio = data['Studio']
    type = data['Type']

    synopsis = description
    vector_synopsis = vectorize_sentence(synopsis)
    final_synopsis = vector_synopsis.sum()
    # Genre
    
    le = LabelEncoder()
    genre_float = le.fit_transform([genre])# Studio
    studio_float = le.fit_transform([studio])# Producer
    producer_float = le.fit_transform([producer])# Title
    title_float = le.fit_transform([title])
    type_float = le.fit_transform([type])
    a=[]
    for i in range(24):
        a.append(random.random())
    predictions = rf_loaded.predict([[float(genre_float), float(final_synopsis), float(producer_float), float(studio_float), float(type_float), float(title_float)] + a])


    return str(predictions[0])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port = 5001)
