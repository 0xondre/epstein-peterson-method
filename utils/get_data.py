import requests
import math

# get distance between points using Haversine formula
def get_distance(start_lat, start_lon, end_lat, end_lon): 
    R = 6371000  # earth radius in meters
    phi1, phi2 = math.radians(start_lat), math.radians(end_lat)
    delta_phi = math.radians(end_lat - start_lat)
    delta_lambda = math.radians(end_lon - start_lon)
    
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c 

def generate_steps(start_lat, start_lon, end_lat, end_lon, step=100): # step in meters
    distance = get_distance(start_lat, start_lon, end_lat, end_lon)
    num_points = int(distance // step)
    steps = {}
    
    for i in range(num_points + 1):
        fraction = i / num_points
        lat = start_lat + (end_lat - start_lat) * fraction
        lon = start_lon + (end_lon - start_lon) * fraction
        if i == num_points:
            steps[round(distance*0.001,3)]={'latitude': round(lat,5), 'longitude': round(lon,5)}
            continue
        steps[round(i*0.1, 1)] = {'latitude': round(lat,5), 'longitude': round(lon,5)}
    
    return steps # {distance:{'latitude':latitude,'longitude':longitude}}

def get_elevation(steps:dict):
    elevations = {}
    points = []
    distances = []

    for k,v in steps.items():
        latitude = v['latitude']
        longitude = v['longitude']
        points.append(f"{latitude},{longitude}")
        distances.append(k)

    points_str = "|".join(points)

    response = requests.get(f'https://api.open-elevation.com/api/v1/lookup?locations={points_str}')

    if response.status_code == 200:
        response_data = response.json()
        results = response_data.get("results", [])

        for i, result in enumerate(results):
            elevations[distances[i]] = result['elevation']

        return elevations
    else:
        print(f"Request failed with status code {response.status_code}")
        return None