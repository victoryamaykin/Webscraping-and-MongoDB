import streamlit as st
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

@app.route("/")
def echo():

    mars_data = mongo.db.mars_data.find_one()
    if mars_data is None:
        return redirect("/scrape")

    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():

    mars_data = mongo.db.mars_data.drop()

    mars_data = scrape_mars.scrape_info()

    mongo.db.mars_data.update({}, mars_data, upsert=True)
    
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
