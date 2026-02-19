import folium
# Your data
vehicle_positions = {
    "Truck_A": (45.5236, -122.6750),
    "Van_B": (45.5285, -122.6121),
    "Car_C": (45.5210, -122.6510)
}

m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# 2. Add points to the map
for vehicle_id, coords in vehicle_positions.items():
    folium.CircleMarker(
        location=coords,
        radius=7,
        popup=vehicle_id,
        color="blue",
        fill=True,
        fill_color="cyan"
    ).add_to(m)

m.save("vehicle_map.html")