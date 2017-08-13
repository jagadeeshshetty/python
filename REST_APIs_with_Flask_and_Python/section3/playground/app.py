#!/anaconda/bin/python
""" It's a learing project."""

from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# POST - used to recive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])   # http://127.0.0.1/strore/some_name
def get_store(name):
    pass


# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def creare_item_in_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store():
    pass

app.run(port=5000)
