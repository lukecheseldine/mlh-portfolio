import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import folium
import json
from folium.plugins import FloatImage

load_dotenv()
app = Flask(__name__)
data = open("app/static/data.json")
data = json.load(data)


# routes send the loaded json object "data" to display personal information
@app.route("/")
def index():
    return render_template(
        "index.html", title="LMS Portfolio", url=os.getenv("URL"), data=data
    )


@app.route("/about")
def about():
    return render_template(
        "about.html", title="LMS Portfolio", url=os.getenv("URL"), data=data
    )


@app.route("/experience")
def experience():
    return render_template(
        "experience.html", title="LMS Portfolio", url=os.getenv("URL"), data=data
    )


@app.route("/map")
def map():
    return render_template(
        "map.html", title="LMS Portfolio", url=os.getenv("URL"), data=data
    )


@app.route("/folium_map")
def folium_map():
    list = [
        {
            "name": "Haleakala National Park, Hawaii",
            "latitude": 20.770250,
            "longitude": -156.239304,
            "color": "blue",
        },
        {
            "name": "La Sagrada Familia, Spain",
            "latitude": 41.546322,
            "longitude": 2.447750,
            "color": "blue",
        },
        {
            "name": "Brighton Palace Pier, UK",
            "latitude": 50.8169,
            "longitude": -0.1367,
            "color": "blue",
        },
        {
            "name": "Grand Teton National Park, USA",
            "latitude": 43.790428,
            "longitude": -110.681763,
            "color": "blue",
        },
        {
            "name": "Orlando, Florida, USA",
            "latitude": 28.538336,
            "longitude": -81.379234,
            "color": "green",
        },
        {
            "name": "New York City, USA",
            "latitude": 40.7127281,
            "longitude": -74.0060152,
            "color": "green",
        },
        {
            "name": "Quebec City, Canada",
            "latitude": 46.829853,
            "longitude": -71.254028,
            "color": "green",
        },
        {
            "name": "Montreal, Canada",
            "latitude": 45.5017,
            "longitude": -73.5673,
            "color": "red",
        },
        {
            "name": "Hyderabad, India",
            "latitude": 17.3850,
            "longitude": 78.4867,
            "color": "red",
        },
        {
            "name": "Doha Qatar",
            "latitude": 25.2854,
            "longitude": 51.5310,
            "color": "red",
        },
    ]

    start_coords = (43.653, -79.383)
    folium_map = folium.Map(location=start_coords, zoom_start=3, tiles="Stamen Terrain")

    for i in range(0, len(list)):
        folium.Marker(
            location=[list[i]["latitude"], list[i]["longitude"]],
            popup=list[i]["name"],
            icon=folium.Icon(color=list[i]["color"]),
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
