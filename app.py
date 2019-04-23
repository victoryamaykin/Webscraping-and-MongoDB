import numpy as np
import pandas as pd

from flask import Flask, render_template

import pymongo
import datetime as dt
from datetime import timedelta




# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db

news_title = soup.body.find
news_p = soup.body.find('p')
featured_image_url = soup.body.find('img')
mars_weather = soup.find.mars_weather
time = dt.datetime.now()

db.mars_db.insert_one({
        'Article Title': news_title,
        'Summary': news_p,
        'Featured Image': featured_image_url,
        'Weather': mars_weather, 
                "Date of entry": time
})


@app.route("/")
def echo():
    return render_template("index.html", text="app.py")

@app.route("/scrape")
def scrape():
    return (app.py)

if __name__ == '__main__':
    app.run(debug=True)