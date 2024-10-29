from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB configuration
client = MongoClient('mongodb://mongo:27017/')
db = client['mydatabase']
collection = db['items']

# Routes
@app.route('/items', methods=['POST']   )
def create_item():
    name = request.json['name']
    item_id = collection.insert_one({'name': name}).inserted_id
    return jsonify({'message': 'Item created', 'id': str(item_id)}), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = collection.find()
    return jsonify([{'id': str(item['_id']), 'name': item['name']} for item in items])

@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    collection.update_one({'_id': ObjectId(id)}, {'$set': {'name': request.json['name']}})
    return jsonify({'message': 'Item updated'})

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
