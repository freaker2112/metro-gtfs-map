import requests
import json
import folium


local_lines = {2,3,4,5,7,9,10,11,14,17,18,22,25,27,30,32,33,36,38,46,54,61,62,63,64,65,67,68,71,72,74,75,80,83,87}
#local_lines = {2,3,4}
UofM_lines = {120,121,122,123,124,125}
lrt_lines = {901,902}
brt_lines = {903,904,905}
abrt_lines = {921,922,923,924,925}
#suburban_lines: {219,223,225,227,250,252,264,270,275,294,323,345,355,363,412,420,436,440,442,444,445,446,447,460}


routes_resp = requests.get('https://svc.metrotransit.org/nextrip/routes', headers={'accept': 'application/json'}).text
routes_dict = json.loads(routes_resp)


def get_vehicle_position(line):
    response = json.loads(requests.get(f'https://svc.metrotransit.org/nextrip/vehicles/{line}', headers={'accept': 'application/json'}).text)
    return response
    
for routenum in local_lines:
    lrt_locations = {row['trip_id']: (row['latitude'], row['longitude']) for row in get_vehicle_position(routenum)}
    print(lrt_locations)

green_lrt_locations = {row['trip_id']: (row['latitude'], row['longitude']) for row in get_vehicle_position(902)}
blue_lrt_locations = {row['trip_id']: (row['latitude'], row['longitude']) for row in get_vehicle_position(901)}


m = folium.Map(location=[44.9757, -93.2694], zoom_start=13)


for trip_id, coords in green_lrt_locations.items():
    folium.CircleMarker(
        location=coords,
        radius=5,
        popup=f"METRO Green Line {trip_id}",
        color="green",
        fill=True,
        fill_color="green"
    ).add_to(m)
for trip_id, coords in blue_lrt_locations.items():
    folium.CircleMarker(
        location=coords,
        radius=5,
        popup=f"METRO Blue Line {trip_id}",
        color="blue",
        fill=True,
        fill_color="blue"
    ).add_to(m)


def addtomap_bus(line):
    line_locations = {row['trip_id']: (row['latitude'], row['longitude']) for row in get_vehicle_position(line)}
    for trip_id, coords in line_locations.items():
        folium.CircleMarker(
            location=coords,
            radius=5,
            popup=f"{line} {trip_id}",
            color="purple",
            fill=True,
            fill_color="purple"
        ).add_to(m)

def addtomap_umnbus(line):
    line_locations = {row['trip_id']: (row['latitude'], row['longitude']) for row in get_vehicle_position(line)}
    for trip_id, coords in line_locations.items():
        folium.CircleMarker(
            location=coords,
            radius=5,
            popup=f"{line} {trip_id}",
            color="maroon",
            fill=True,
            fill_color="yellow"
        ).add_to(m)

def addtomap_aBRT(line):
    line_locations = {row['trip_id']: (row['latitude'], row['longitude']) for row in get_vehicle_position(line)}
    if line == 925:
        linename = "METRO E Line"
    if line == 922:
        linename = "METRO B Line"
    if line == 921:
        linename = "METRO A Line"
    if line == 923:
        linename = "METRO C Line"
    if line == 924:
        linename = "Metro D Line"
    for trip_id, coords in line_locations.items():
        folium.CircleMarker(
            location=coords,
            radius=5,
            popup=f"{linename} {trip_id}",
            color="gray",
            fill=True,
            fill_color="gray"
        ).add_to(m)

def addtomap_BRT(line):
    line_locations = {row['trip_id']: (row['latitude'], row['longitude']) for row in get_vehicle_position(line)}
    if line == 904:
        linename = "METRO Orange Line"
        linecolor = "orange"
    if line == 905:
        linename = "METRO Gold Line"
        linecolor = "yellow"
    if line == 903:
        linename = "METRO Red Line"
        linecolor = "red"
    for trip_id, coords in line_locations.items():
        folium.CircleMarker(
            location=coords,
            radius=5,
            popup=f"{linename} {trip_id}",
            color=linecolor,
            fill=True,
            fill_color=linecolor
        ).add_to(m)


for linenum in local_lines:
    addtomap_bus(linenum)
for linenum in abrt_lines:
    addtomap_aBRT(linenum)
for linenum in UofM_lines:
    addtomap_umnbus(linenum)
for linenum in brt_lines:
    addtomap_BRT(linenum)

m.save("vehicle_map.html")
