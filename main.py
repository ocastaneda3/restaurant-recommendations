import config   # API Key

import requests     # HTTP Request
import json         # JSON
import geocoder     # Geocoder

import random

from sspipe import p, px

def main():
    # Current Locatoins
    current_loc = get_current_loc()

    # CSUF Loaction
    # current_loc = [33.8829, -117.8869]

    data_ = 'simiulated_data_stream.txt' | p(read_file) | p(generate_nodes)

    for x in data_:
        print('New Incoming Orders:\n-------------------')

        print('Request ID:\t{}\nUser ID:\t{}\nRestaurant:\t{}\nItem:\t\t{}\nPrice:\t\t${}\n'.format(x['request_id'], x['user_id'], x['payload']['restaurant_name'], x['payload']['item']['name'], x['payload']['item']['price']))
        print('\nAnalyzing . . .\n\n')
        print('Recommendation:')
        recommended_res = x['payload']['restaurant_name'] | p(get_restaurant_alias, px) | p(get_recommendation, px, current_loc[0], current_loc[1])
        recommended_menu = recommended_res['name'] | p(get_restaurant_id, px, current_loc[0], current_loc[1]) | p(get_restaurant_menu, px)

        print('Restaurant:\t{}\nItem:\t\t{}\n'.format(recommended_res['name'], recommended_menu['menu_item_name']))

def get_restaurant_id(restaurant_name, latitude_, longitude_):
    url = 'https://us-restaurant-menus.p.rapidapi.com/restaurants/search/ids'

    params = {'distance':'5','page':'1','q':restaurant_name, 'lat':latitude_, 'lon':longitude_}

     # Making a get request to the API
    response = requests.get(url, headers=config.headers_menu, params=params)

    return json.loads(response.text)['result']['data'][0]['restaurant_id']

def get_restaurant_menu(restaurant_id):
    url = 'https://us-restaurant-menus.p.rapidapi.com/restaurant/{}/menuitems'.format(restaurant_id)

    params = {'page':'1'}

    # Making a get request to the API
    req = requests.get(url, headers=config.headers_menu, params=params)

    parse = json.loads(req.text)
    rand_menu_item = parse['result']['data'][random.randint(0, len(parse['result']['data']) - 1)]

    return rand_menu_item

def get_current_loc():
    return geocoder.ip('me').latlng

def get_recommendation(restaurant_type, latitude_, longitude_):
    url ='https://api.yelp.com/v3/businesses/search'

    # In the dictionary, restaurant type is stored to be found within 1000 meters of the latitude and longitude provided
    params = {'term':restaurant_type, 'latitude':latitude_, 'longitude':longitude_, 'radius':'5000', 'sort_by':'distance', 'limit':'25'}

    # Making a get request to the API
    req = requests.get(url, params=params, headers=config.headers_yelp)

    parse = json.loads(req.text)

    rand_int = random.randint(0, len(parse['businesses']) - 1)

    return parse['businesses'][rand_int]

def get_restaurant_alias(restaurant_name):
    url ='https://api.yelp.com/v3/businesses/search'

    # In the dictionary, term can take values like food, cafes or businesses like McDonalds
    params = {'term':restaurant_name, 'location':'Fullerton', 'limit':'1'}

    # Making a get request to the API
    req = requests.get(url, params=params, headers=config.headers_yelp)

    parse = json.loads(req.text)

    return parse['businesses'][0]['categories'][0]['alias']

def generate_nodes(list_):
    data_ = []
    for x in list_:
        item_ = {}
        item_.update({'name':x[3], 'price':x[4]})
        payload_ = {}
        payload_.update({'restaurant_name':x[2], 'item':item_})
        data_.append({'request_id':x[0], 'user_id':x[1], 'payload':payload_})

    return data_

def read_file(input_file):
    with open(input_file) as in_file:
        read_data = in_file.read()

    data_buffer = []
    for x in read_data.split('\n\n'):
        data_buffer.append(x.split('\n'))

    return data_buffer

if __name__ == "__main__":
    main()