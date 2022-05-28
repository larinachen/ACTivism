from flask import Flask
from flask import render_template, request
import requests
from pprint import pprint

# initializes flask app:
app = Flask(__name__)

@app.route('/')
def exercise1():
    return '''
        <!DOCTYPE html>
        <html lang="en" >
        <head>
            <meta charset="UTF-8">
            <title>Demo</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css">
            <link rel="stylesheet" href="/static/style.css">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body>
            <h1>Hello </h1>
        </body>
        </html>
    '''
# enables flask app to run using "python3 app.py"
if __name__ == '__main__':
    app.run()
