from flask import Flask
from flask import render_template, request
import requests
from pprint import pprint

# initializes flask app:
app = Flask(__name__)

@app.route('/')
def exercise1():
    return render_template(
        'api/api_tester.html'
    )
    
# enables flask app to run using "python3 app.py"
if __name__ == '__main__':
    app.run()
