from unicodedata import category
from flask import Flask, render_template, jsonify
from flask import render_template, request
from flask_cors import CORS
from itsdangerous import Serializer
from matplotlib.backend_bases import LocationEvent
from pandas import describe_option #comment this on deployment
import requests
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
import os
import pickle
from pprint import pprint

# initializes flask app:
app = Flask(__name__,template_folder='client-side/public')

# set up database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password0202@localhost/ACTivism"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# cors = CORS(app, 
#     resources={r"/api/*": {"origins": '*'}}, 
#     supports_credentials=True
# )

# set up database tables
class Events(db.Model):


    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.Text(), nullable = False)
    description = db.Column(db.Text(), nullable = True)
    location = db.Column(db.Text(), nullable = False)
    organizer = db.Column(db.Text(), nullable = False)
    time = db.Column(db.Text(), nullable = False)
    link = db.Column(db.Text(), nullable = True)
    category = db.Column(db.Text(), nullable = False)
    img_url = db.Column(db.Text(), nullable = True)
    keyword = db.Column(db.Text(), nullable = False) # will need to change to keywordS

    def __init__(self, title, description, location, organizer, time, link, category, img_url, keyword):
        self.title = title
        self.description = description
        self.location = location
        self.organizer = organizer
        self.time = time
        self.link = link
        self.category = category
        self.img_url = img_url
        self.keyword = keyword
        


    def __repr__(self):
        return '<Bookmark %r>' % self.id     

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.limit(10).all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_keyword(cls, keyword):
        return cls.query.filter_by(keyword=keyword).limit(10).all()

    

class EventsSchema(Schema):
    title = fields.String()
    description = fields.String()
    location = fields.String()
    organizer = fields.String()
    time = fields.String()
    link = fields.String()
    category = fields.String()
    img_url = fields.String()
    keyword = fields.String()

@app.route('/')
def home():
    return render_template(
        'index.html',
        keywords = ["a","b"]
    )

@app.route('/tester')
def index():
    k = 'a'
    return render_template(
        'api_tester.html',
    )


@app.route('/organizers')
def organizers():
    return render_template(
        'organizers.html',
    )

@app.route('/events', methods=['GET'])
def get_all_events():
    events = Events.get_all()
    serializer = EventsSchema(many=True)
    data = serializer.dump(events)
    data = jsonify(data)
    return data

@app.route('/events', methods=['POST'])
def create_an_event():
    data = request.get_json()
    new_event = Events(
        title = data.get('title'),
        description = data.get('description'),
        location = data.get('location'),
        organizer= data.get('organizer'),
        time= data.get('time'),
        link= data.get('link'),
        category = data.get('category'),
        img_url = data.get('img_url'),
        keyword= data.get('keyword')
    )

    new_event.save()
    serializer = EventsSchema()
    data = serializer.dump(new_event)
    data = jsonify(data)
    return data,201
    
# enables flask app to run using "python3 app.py"
if __name__ == '__main__':
    app.run(debug=True)
