#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""

import requests
import time
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"

def main():
    resp= requests.get(URL).json()
    
    #{'message': 'success', 'timestamp': 1664377254, 'iss_position': {'latitude': '7.0840', 'longitude': '125.8619'}}
    
    #position
    lat = resp['iss_position']['latitude']
    lon = resp['iss_position']['longitude']    
    tm = time.ctime(resp['timestamp'])
    coords= (lat, lon)
    location = rg.search(coords)
    name = location[0]['name']
    country = location[0]['cc']

    #prints out position
    print(f'THE CURRENT LOCATION OF ISS:\n Timestamp:{tm}\n Lon: {lon}\n Lat: {lat}\n Location: {name}, {country}')
        
if __name__ == "__main__":
    main()
