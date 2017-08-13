#!/anaconda/bin/python
""" It's a learing project."""

from flask import Flask

app = Flask(__name__)


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
# POST /store/<string:name>/item
# GET /store/<string:name>/item



app.run(port=5000)
