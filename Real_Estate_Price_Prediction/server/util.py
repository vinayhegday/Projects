import json
import pickle
import numpy as np


data_columns = None
locations = None
_model = None

def get_location_names():
    return locations

def load_saved_atrifacts():

    global data_columns
    global locations
    global _model

    with open('./server/Artifacts/columns.json', 'r') as f:
        data_columns = json.load(f)['data_column']
        locations = data_columns[3:]
    with open('./server/Artifacts/house_price_predictor.pickle', 'rb') as f:
        _model = pickle.load(f)

    print('Loading the artifacts is done')


def get_estimated_price(location, sqft, bhk, bath):

    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(_model.predict([x])[0], 2)


if __name__ == "__main__":
    load_saved_atrifacts()
    print(get_location_names())
    print(get_estimated_price('kammanahalli', 1300, 3, 3))