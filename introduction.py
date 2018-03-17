#! /usr/bin/env python
from pygeocoder import Geocoder
import requests


def get_geocode(address):
    paramaters = {'address':address, 'sensor':False}
    base = 'http://maps.google.com/maps/api/geocode/json'
    response = requests.get(base, paramaters)
    answer  = response.json()
    print(answer)



if __name__ == "__main__":
    address = '207 N. Defiance St, Archbold, OH'
    print(Geocoder.geocode(address)[0].coordinates)
    get_geocode(address)




