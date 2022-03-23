#route modules
import openrouteservice
from openrouteservice import convert
import json
import folium

#geocode modules
from geopy.geocoders import Nominatim

#variables to store locational data
coordLong = ""
coordLat = ""

endCoordLat = ""
endCoordLong = ""

#takes address and converts to latitude and longitude to use in distance calculation
def coordGet(startLocation, endLocation):
    global coords
    global coordLat
    global coordLong
    global endCoordLat
    global endCoordLong

    geolocator = Nominatim(user_agent="alevel-application")
    coords = geolocator.geocode(startLocation)
    coordLat = coords.latitude
    coordLong = coords.longitude
    endCoords = geolocator.geocode(endLocation)
    endCoordLat = endCoords.latitude
    endCoordLong = endCoords.longitude

def routing():
    #starting point coords
    global coordLong
    global coordLat
    #end point coords
    global endCoordLat
    global endCoordLong

    #sets a list to the corresponding values for coordinates
    coords = ((coordLong, coordLat), (endCoordLong,endCoordLat))
    client = openrouteservice.Client(key='5b3ce3597851110001cf62488cb4c056c9294a4ba1a5a37393b69413')
    #calls from the API
    res = client.directions(coords)
    #tested json response
    with(open('test.json','+w')) as f:
        f.write(json.dumps(res,indent=4, sort_keys=True))

    #takes geometry from json, decodes it for use in map
    geometry = client.directions(coords)['routes'][0]['geometry']
    decoded = convert.decode_polyline(geometry)

    #configures map settings
    m = folium.Map(location=[coordLat, coordLong],zoom_start=15, control_scale=True,tiles="cartodbpositron")
    #creates and saves map
    folium.GeoJson(decoded).add_to(m)
    m.save('map.html')

coordGet("19 Langsett court Doncaster", "2 Littleworth lane Doncaster")
routing()