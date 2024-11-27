from epsteinpeterson.peaks import get_ep_peak
from epsteinpeterson.attenuation import calculate_attenuation
from utils.get_data import generate_steps,get_elevation 


# FOR NOW HARDCODED, CHANGE IT INTO flask later
start_lat, start_lon = 49.809596,19.052732
end_lat, end_lon = 49.699071,19.269432

steps = generate_steps(start_lat, start_lon,end_lat, end_lon)
distance_height=get_elevation(steps)

peaks = get_ep_peak(distance_height, {})
print("Peaks needed in epstein-peterson method:",peaks)

attenuation, params = calculate_attenuation(distance_height,peaks,450)
print("Attenuation:",attenuation)
print(params)