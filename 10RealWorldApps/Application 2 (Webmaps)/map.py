import folium, pandas

data =  pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])
html = """
<h4>Volcano name:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a></h4><br>
Height: %s m
"""

def icon_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[55.587032, 37.672990], zoom_start=6, tiles='Stamen Terrain')

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html = html % (nm, nm, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), fill_color=icon_color(el), color='gray', fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Map1.html')
