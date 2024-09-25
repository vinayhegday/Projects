from flask import Flask, jsonify, request
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_location_names')
def get_location_names():
    # Assuming `get_location_names` is a function in the `util` module
    locations = util.get_location_names()
    print(locations)
    response = jsonify({
        'locations': locations
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        
        # Assuming `get_estimated_price` is a function in the `util` module
        estimated_price = util.get_estimated_price(location, total_sqft, bedrooms, bathrooms)
        
        response = jsonify({
            'estimated_price': estimated_price
        })
        return response

    except Exception as e:
        # Basic error handling
        return jsonify({
            'error': str(e)
        }), 400

if __name__ == "__main__":
    print('Starting the server for house price prediction')
    util.load_saved_atrifacts()
    app.run(debug=True)  # Added debug=True for development
