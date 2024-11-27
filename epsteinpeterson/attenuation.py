import math

def calculate_attenuation(steps:dict, peaks:dict, f:float):
    transmitter_k,transmitter_v = next(iter(steps.items()))
    receiver_k,receiver_v = next(reversed(steps.items()))

    peaks = peaks | {transmitter_k:transmitter_v,receiver_k:receiver_v}
    peaks = {k: peaks[k] for k in sorted(peaks)}
    
    distances = list(peaks.keys())
    heights = list(peaks.values())
    
    a_sum = 0
    lam = 300000000.0/(f*1000000)
    params = []

    for i in range(len(distances)):
        if i == 0 or i == len(distances)-1:
            continue
        
        h = (heights[i]-heights[i-1])-(distances[i]-distances[i-1])*1000*(heights[i+1]-heights[i-1])/((distances[i]-distances[i-1])*1000+(distances[i+1]-distances[i])*1000)
        v = h * math.sqrt(2*((distances[i]-distances[i-1])+(distances[i+1]-distances[i]))*1000/(lam*(distances[i]-distances[i-1])*1000*(distances[i+1]-distances[i])*1000))
        a = 6.9 + 20*math.log10(math.sqrt((v-0.1*0.1)*(v-0.1*0.1)+1)+v-0.1)

        params.append({'Distance from transmitter':distances[i],'A':round(a,2),'v':round(v,2),'h':round(h,2)})

        a_sum += a
    return a_sum, params