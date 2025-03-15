from flask import Flask, render_template, redirect, url_for, flash
import os

import requests

PORT = int(os.environ.get('PORT', 9000))

BACKEND_URL = os.environ.get('BACKEND_URL','http://localhost:8000')

app = Flask(__name__)

@app.route('/')
def index():
    
    response = requests.get(f'{BACKEND_URL}/api/get')
    
    data = response.json()
    
    print(data, type(data))    
    
    env = dict(os.environ)
    
    return render_template('index.html', env = env, data = data['data'])

if __name__ == '__main__':
    app.run(debug=True, port=PORT,host='0.0.0.0')