import folium
import overpy
import osmnx
import json
import requests
import osm2geojson



relation_id = relation_id = 2439373 

# Overpass API query with 'out geom' to include full geometry information
# We request the data in XML format for compatibility with osm2geojson
overpass_url = "https://overpass-api.de/api/interpreter"
overpass_query = f"""
[out:xml][timeout:25];
rel({relation_id});
out geom;
"""

# Make the request to the Overpass API
try:
    response = requests.get(overpass_url, params={'data': overpass_query}, timeout=25)
    response.raise_for_status() # Raise an exception for bad status codes
    osm_xml = response.text

    # Convert the OSM XML data to GeoJSON
    geojson_data = osm2geojson.xml2geojson(osm_xml, filter_used_refs=False)

    # Print or save the GeoJSON data
    print(json.dumps(geojson_data, indent=2))

    # Optional: Save to a file
    with open(f'relation_{relation_id}.geojson', 'w') as f:
        json.dump(geojson_data, f, indent=2)

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from Overpass API: {e}")
except Exception as e:
    print(f"An error occurred during conversion: {e}")
 

# Overpass API query with 'out geom' to include full geometry information
# We request the data in XML format for compatibility with osm2geojson
overpass_url = "https://overpass-api.de/api/interpreter"
overpass_query = f"""
[out:xml][timeout:30];
rel({relation_id});
out geom;
"""

# Make the request to the Overpass API
try:
    response = requests.get(overpass_url, params={'data': overpass_query}, timeout=30)
    response.raise_for_status() # Raise an exception for bad status codes
    osm_xml = response.text

    # Convert the OSM XML data to GeoJSON
    geojson_data = osm2geojson.xml2geojson(osm_xml, filter_used_refs=False)

    # Print or save the GeoJSON data
    print(json.dumps(geojson_data, indent=2))

    # Optional: Save to a file
    with open(f'relation_{relation_id}.geojson', 'w') as f:
        json.dump(geojson_data, f, indent=2)

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from Overpass API: {e}")
except Exception as e:
    print(f"An error occurred during conversion: {e}")
