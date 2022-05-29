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




# initializes flask app:
app = Flask(__name__)

# set up database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password0202@localhost/ACTivism"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

cors = CORS(app, 
    resources={r"/api/*": {"origins": '*'}}, 
    supports_credentials=True
)

# set up database tables
class Events(db.Model):


    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.Text(), nullable = False)
    description = db.Column(db.Text(), nullable = True)
    location = db.Column(db.Text(), nullable = False)
    organizer = db.Column(db.Text(), nullable = False)
    time = db.Column(db.Text(), nullable = False)
    link = db.Column(db.Text(), nullable = True)
    keyword = db.Column(db.Text(), nullable = False) # will need to change to keywordS

    def __init__(self, title, description, location, organizer, time, link, keyword):
        self.title = title
        self.description = description
        self.location = location
        self.organizer = organizer
        self.time = time
        self.link = link
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
    keyword = fields.String()

@app.route('/tester')
def index():
    search_term = request.args.get('term')
    search_limit = request.args.get('limit') or 1
    url = 'https://www.apitutor.org/spotify/simple/v1/search?q={term}&type=track&limit={limit}'.format(term=search_term, limit=search_limit)
    response = requests.get(url)
    tracks = response.json()
    return render_template(
        'api_tester.html',
        track = tracks[0]
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
