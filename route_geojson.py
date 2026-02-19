import requests
import json
import folium
import overpy
import osmnx
import osm2geojson

ovapi = overpy.Overpass()

local_lines = {2,3,4,5,7,9,10,11,14,17,18,22,25,27,30,32,33,36,38,46,54,61,62,63,64,65,67,68,71,72,74,75,80,83,87}
UofM_lines = {120,121,122,123,124,125}
lrt_lines = {901,902}
brt_lines = {903,904,905}
abrt_lines = {921,922,923,924,925}
#suburban_lines: {219,223,225,227,250,252,264,270,275,294,323,345,355,363,412,420,436,440,442,444,445,446,447,460}


m = folium.Map(location=[44.9757, -93.2694], zoom_start=13)


with open('route_data/mspgeom.oapi', 'r', encoding='utf-8') as f:
    overpass_data = json.load(f)
with open('route_data/blueline.oapi', 'r', encoding='utf-8') as f:
    overpass_data_lrt_blue = json.load(f)
with open('route_data/greenline.oapi', 'r', encoding='utf-8') as f:
    overpass_data_lrt_green = json.load(f)
with open('route_data/orangeline.oapi', 'r', encoding='utf-8') as f:
    overpass_data_brt_orange = json.load(f)
with open('route_data/abrt.oapi', 'r', encoding='utf-8') as f:
    overpass_data_abrt = json.load(f)
with open('route_data/goldline.oapi', 'r', encoding='utf-8') as f:
    overpass_data_brt_gold = json.load(f)
with open('route_data/express.oapi', 'r', encoding='utf-8') as f:
    overpass_data_exprs = json.load(f)

geo_data = osm2geojson.json2geojson(overpass_data)
geo_data_lrt_blue = osm2geojson.json2geojson(overpass_data_lrt_blue)
geo_data_lrt_green = osm2geojson.json2geojson(overpass_data_lrt_green)
geo_data_brt_orange = osm2geojson.json2geojson(overpass_data_brt_orange)
geo_data_abrt = osm2geojson.json2geojson(overpass_data_abrt)
geo_data_brt_gold = osm2geojson.json2geojson(overpass_data_brt_gold)
geo_data_exprs = osm2geojson.json2geojson(overpass_data_exprs)

folium.GeoJson(
    geo_data,
    name='Routes',
    color='purple'
).add_to(m)

folium.GeoJson(
    geo_data_lrt_blue,
    name='Routes',
    color='blue'
).add_to(m)

folium.GeoJson(
    geo_data_lrt_green,
    name='Routes',
    color='green'
).add_to(m)

folium.GeoJson(
    geo_data_brt_orange,
    name='Routes',
    color='orange'
).add_to(m)

folium.GeoJson(
    geo_data_abrt,
    name='Routes',
    color='gray'
).add_to(m)

folium.GeoJson(
    geo_data_brt_gold,
    name='Routes',
    color='yellow'
).add_to(m)

folium.GeoJson(
    geo_data_exprs,
    name='Routes',
    color='pink',
    opacity=0.5
).add_to(m)

folium.LayerControl().add_to(m)
m.save('converted_overpass_map.html')
print("Map saved to converted_overpass_map.html")
