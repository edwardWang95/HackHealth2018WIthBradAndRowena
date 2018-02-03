import folium
import os
import pandas

def createMap():
    map = folium.Map(location=[45.5236, -122.6750])
    dirname, filename = os.path.split(os.path.abspath(__file__))
    #print(dirname)
    #map.save(dirname + '/map.html')

    state_geo = r'us-states.json'
    state_unemployment = r'US_Unemployment_Oct2012.csv'

    state_data = pandas.read_csv(state_unemployment)

    # Let Folium determine the scale
    map = folium.Map(location=[48, -102], zoom_start=3)
    map.geo_json(geo_path=state_geo, data=state_data,
                 columns=['State', 'Unemployment'],
                 key_on='feature.id',
                 fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2,
                 legend_name='Unemployment Rate (%)')
    map.save(dirname + '/map.html')

createMap()
