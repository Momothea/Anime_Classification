import unittest
from flask import render_template
import sys
import requests, json

sys.path.insert(1, './flask_web_application')


#from website import create_app
from  main import app



class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_classify_GET(self):
        response = self.app.get('/classify')
        self.assertEqual(response.status_code, 200)

    #def test_classify_POST(self):
        #response = self.app.get('/classify')
        #data = {'Title':"Title",
        #        'Genre':"Genre",
        #          'Description':"Description",
        #          'Producer':"Producer",
        #          'Studio':"Studio",
        #          'Type': "Type"}
        
        #json_data = json.dumps(data)
        #headers = {'Content-Type': 'application/json'}
        #response = requests.post("http://localhost:5000/classify", json=json_data, headers=headers)
        #self.assertEqual(response.status_code, 201)

            #{"prediction": "T-shirt/top",
            #"predicted_array": [[1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]]}

 

if __name__ == '__main__':
    unittest.main()