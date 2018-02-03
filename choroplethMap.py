import folium
import os
import pandas

def createMap():
    map = folium.Map(location=[45.5236, -122.6750])
    dirname, filename = os.path.split(os.path.abspath(__file__))
    print(dirname)
    map.save(dirname + '/map.html')


createMap()