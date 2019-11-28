from flask import Flask
from populate_library import full_catalogue
import json
app = Flask("marconi")

@app.route("/")
def data_book():
    return json.dumps(
        
        # create a list with all the books in the catalogue
        # book.__dict__ create a json with all the variables of the class Book
        [book.__dict__ for book in full_catalogue]
        
        )