from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def echo():
    mars_data = mongo.db.collection.find_one()
    return render_template("index.html", data=mars_data)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info()
    mongo.mars_db.collection.update({}, mars_data, upsert=True)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)