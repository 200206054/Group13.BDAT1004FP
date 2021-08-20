import time
from requests import get
from flask import Flask,render_template, request
from pymongo import MongoClient
import requests

MyIP = get('https://api.ipify.org').text #API to get public IP
api_key = 'a45Wa_FO6lGz4g31O4OuDdSuItx0L5WKa5itBuOhC1s' 

IpForLocation = "http://ip-api.com/json/"+MyIP #variable that combines an API for location with public IP above

client = MongoClient("mongodb+srv://pallavi:Ekansh%402089@cluster0.23h5o.mongodb.net/coordinates?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.coordinates
records = db.coordinates

r = requests.get(IpForLocation)
if r.status_code == 200: #200 is a standardized status code in HTTPS. It tells that everything on the API is good to go
    data = r.json() #this data variable will be equal to the request in json format (json is human readable file format)

    records.insert_one(data)
    dataz = list(records.find({},{ "_id": 0, "lat": 1}))
    datalon = list(records.find({},{ "_id": 0, "lon": 1}))

    latitudestr = dataz[-1]
    latitude = latitudestr.get("lat")

    longitudestr = datalon[-1]
    longitude = longitudestr.get("lon")

    print(latitude)

else:
    exit()


app = Flask(__name__)
@app.route('/')

def map_func():
    return render_template('map.html',apikey=api_key,latitude=latitude,longitude=longitude)

if __name__ == '__main__':
    app.run(debug = False)