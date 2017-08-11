#!/anaconda/bin/python
""" It's a learing project."""

from flask import Flask

app = Flask(__name__)

@app.route('/') # 'http://www.googl.com/'
def home():
    return 'Hello, Universe :-)'

app.run(port=5000)
