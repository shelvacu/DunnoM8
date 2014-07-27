import urllib
import json
base_url = "http://api.openweathermap.org/data/2.5/"

def get_weather(city):
    "Queries openweathermap for the given city/location. Returns JSON"
    return json.loads(urllib.request.urlopen(base_url+"weather?q="+city).read())
