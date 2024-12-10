from epsteinpeterson.peaks import get_ep_peak
from epsteinpeterson.attenuation import calculate_attenuation
from utils.get_data import generate_steps,get_elevation
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/calculate',methods=['POST'])
def get_attenuation():
    try:
        start_lat, start_lon = float(request.form['lat1']),float(request.form['long1'])
        end_lat, end_lon = float(request.form['lat2']),float(request.form['long2'])
        
        steps = generate_steps(start_lat, start_lon,end_lat, end_lon)
        distance_height=get_elevation(steps)
        peaks = get_ep_peak(distance_height, {})
        attenuation, params = calculate_attenuation(distance_height,peaks,450)

        return f"Calculated attenuation is equal to {round(attenuation,2)} dB"
    except ValueError:
        return "Invalid input! Please enter valid numbers."

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4200)