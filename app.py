from flask import Flask
from populate_library import json_string

app = Flask("marconi")

@app.route("/")
def data_book():
    return json_string

