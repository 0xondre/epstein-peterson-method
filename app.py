from epsteinpeterson.peaks import get_ep_peak
from epsteinpeterson.attenuation import calculate_attenuation
from utils.process_csv import csv_to_dict 

peaks = get_ep_peak(csv_to_dict(), {})
print("Peaks needed in epstein-peterson method:",peaks)

attenuation, params = calculate_attenuation(csv_to_dict(),peaks,450)
print("Attenuation:",attenuation)
print(params)