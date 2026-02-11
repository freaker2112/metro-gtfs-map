import requests
import json


lines: {2, }

routes_resp = requests.get('https://svc.metrotransit.org/nextrip/routes', headers={'accept': 'application/json'}).text



def get_vehicle_position(line):
    response = requests.get(f'https://svc.metrotransit.org/nextrip/vehicles/{line}', headers={'accept': 'application/json'}).text
    return response
    

print(json.loads(get_vehicle_position(4)))
