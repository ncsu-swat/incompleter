#Source: https://stackoverflow.com/questions/62232259/python3-returning-typeerror-expected-string-or-bytes-like-object
import googlemaps
from timezonefinder import TimezoneFinder
from dateutil import tz 
import arrow as ar

gmaps = googlemaps.Client(key="GOOGLE_API")

lat = 0
lon = 0
tf = TimezoneFinder()

def timeZone(region):
    global lat, lon
    lat = 0
    lon = 0
    try:
        lat = extract_values(gmaps.geocode(region), "latitude" or "lat")[1]
        lon = extract_values(gmaps.geocode(region), "longitude" or "lng")[1]
    except IndexError:
        print("query incorrect. please try again.")
        lat = 0
        lon = 0
    return(tf.timezone_at(lng=lon, lat=lat))

# Extracts all key values from a dictionary obj
def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

utc = ar.utcnow()
location = input("Enter a city for the time zone it's in. ")
region = timeZone(location)
print(region) # returns None
shifted = utc.to(region)
formatted = shifted.format("HH:mm:ss")

print("time in", location, "is:", formatted)