import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import base64
import os.path
from datetime import date

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

@app.route('/upload', methods=['POST'])
def getting_file():
    # getting base64 string over https request
    base64_string = request.json['base64String']

    # remove URI prefix to get base64 data
    base64_data = base64_string.split(',')
    ipynb_data = base64.b64decode(base64_data[1])

    # getting system time
    today = date.today
    d4 = today.strftime("%b-%d-%Y")

    # save file in container
    with open(d4 + '.ipynb', 'wb') as f:
        f.write(ipynb_data)

    return Flask.jsonify({'response': ipynb_data})

# otter assign
# otter grade -> GET
#
# otter generate (not really necessary because it is invisibly done by otter assign)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
