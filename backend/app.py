from flask import Flask, render_template,jsonify
from connections import coll
import os

app = Flask(__name__)

# PORT = os.environ.get('PORT', 3000)
PORT = int(os.environ.get('PORT', 8000))

@app.route('/')
def index():
    
    return jsonify({"messages":"Backend is ruuning"})

@app.route('/api/get')
def api():
    names = coll.find()
    
    result = []

    for name in names:
        result.append(name['value'])
    
    result = {
        'data':result
    }
    return jsonify(result)

@app.route('/api/add/<name>')
def add(name):
    
    coll.insert_one({'value':name})
    
    return jsonify({'message':'Added '+name})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
