from epsteinpeterson.peaks import get_ep_peak
from utils.process_csv import csv_to_dict 

print(get_ep_peak(csv_to_dict(), {}))