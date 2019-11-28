from flask import Flask
from populate_library import full_catalogue
import json
app = Flask("marconi")

@app.route("/")
def data_book():
    return json.dumps([b.__dict__ for b in full_catalogue])