from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('horoscope.html')

@app.route('/horoscope', methods=['POST'])
def horoscope():
    sign = request.form['sign']
    url = f"https://astrology-api.example.com/horoscope?sign={sign}"
    response = requests.get(url)
    horoscope_data = response.json()
    
    return render_template('horoscope.html', horoscope=horoscope_data['horoscope'])

if __name__ == '__main__':
    app.run(debug=True)

