import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import folium
import json
from folium.plugins import FloatImage
from peewee import *
from datetime import datetime
from playhouse.shortcuts import model_to_dict


load_dotenv()
app = Flask(__name__)
data = open("app/static/data.json")
data = json.load(data)

if os.getenv("TESTING") == "true":
    print("Running is test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

############################################################
######################## PAGE ROUTES #######################
############################################################

@app.route("/")
def index():
    return render_template(
        "index.html", title="Team Jungle Portfolio", url=os.getenv("URL"), data=data
    )


@app.route("/about")
def about():
    return render_template(
        "about.html", title="Team Jungle Portfolio", url=os.getenv("URL"), data=data
    )


@app.route("/experience")
def experience():
    return render_template(
        "experience.html",
        title="Team Jungle Portfolio",
        url=os.getenv("URL"),
        data=data,
    )


@app.route("/map")
def map():
    return render_template(
        "map.html", title="Team Jungle Portfolio", url=os.getenv("URL"), data=data
    )

@app.route("/folium_map")
def folium_map():

    start_coords = (43.653, -79.383)
    folium_map = folium.Map(location=start_coords, zoom_start=3, tiles="Stamen Terrain")

    for i in range(0, len(data["locations"])):
        folium.Marker(
            location=[data["locations"][i]["latitude"], data["locations"][i]["longitude"]],
            popup=data["locations"][i]["name"],
            icon=folium.Icon(color=data["locations"][i]["color"]),
        ).add_to(folium_map)

    ## fix mobile view
    folium_map.get_root().header.add_child(
        folium.Element(
            '<meta name="viewport" content="width=device-width,'
            ' initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />'
        )
    )

    image_file = "/static/img/legend.jpg"
    FloatImage(image_file, bottom=0, left=0).add_to(folium_map)

    folium_map.save("app/templates/map.html")
    return render_template("mapindex.html")

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")

############################################################
######################## API ROUTES ########################
#############################################################

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    try:
        name = request.form['name']
        if (name == "" or name == None):
            return 'Invalid name', 400
    except:
        return 'Invalid name', 400
    try:
        email = request.form['email']
        if (not ("@" in email and "." in email) or email == "" or email == None):
            return 'Invalid email', 400
    except:
        return 'Invalid email', 400
    try:
        content = request.form['content']
        if (content == "" or content == None):
            return 'Invalid content', 400
    except:
        return 'Invalid content', 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    mydb.session_commit
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p) 
            for p in 
TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_time_line_post():
    id_to_delete = request.form['id']
    TimelinePost.delete().where(TimelinePost.id == id_to_delete).execute()
    return f'deleted id number {id_to_delete}'

@app.route('/api/timeline_post', methods=['PURGE'])
def purge_time_line_post():
    TimelinePost.delete().execute()
    return "purged timeline"
