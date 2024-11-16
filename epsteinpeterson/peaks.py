def calculate_peak(steps: dict):
    if not steps:
        return None

    fk, fv = next(iter(steps.items())) # first peak
    lk, lv = next(reversed(steps.items())) # last peak
    peaks_over_los = {}

    for k, v in steps.items():
        if k == next(reversed(steps)) or k == next(iter(steps)): # skip first and last pls work
            continue
        h = (v-fv)-(k-fk)*1000*(lv-fv)/((k-fk)*1000+(lk-k)*1000)
        if k == 6.1:
            print(h)
        if h > 0.34:
            peaks_over_los = peaks_over_los | {k: h}
 
    if not peaks_over_los:
        return None

    peak_key = max(peaks_over_los, key=peaks_over_los.get)
    return peak_key

def split_dict(steps: dict, peak_key):
    keys_before_peak = {k: v for k, v in steps.items() if k <= peak_key}
    keys_after_peak = {k: v for k, v in steps.items() if k >= peak_key}
    
    return keys_before_peak, keys_after_peak

def get_ep_peak(steps: dict,peaks: dict):
    if not steps:
        return peaks

    peak_key = calculate_peak(steps)
    print(peak_key)

    if peak_key is None:
        return peaks

    peaks[peak_key] = steps[peak_key]

    before_peak, after_peak = split_dict(steps, peak_key)

    peaks = get_ep_peak(before_peak, peaks)
    peaks = get_ep_peak(after_peak, peaks)

    return peaks