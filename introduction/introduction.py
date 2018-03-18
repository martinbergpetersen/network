#! /usr/bin/env python
import http.client
import json
import socket
from urllib.parse import quote_plus

import requests
from pygeocoder import Geocoder  # NOQA

BASE = '/maps/api/geocode/json'

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n\
Host: maps.google.com:80\r\n\
User-Agent: search4.py (Foundations of Python Network Programming)\r\n\
Connection: close\r\n\
\r\n\
"""


def get_geocode_3(address):
    sock = socket.socket()
    sock.connect(('maps.google.com', 80))
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))


def get_geocode_2(address):
    path = '{}?address={}?sensor=false'.format(BASE, quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply)


def get_geocode(address):
    paramaters = {'address': address, 'sensor': False}
    base = 'http://maps.google.com/maps/api/geocode/json'
    response = requests.get(base, paramaters)
    answer = response.json()
    print(answer)


if __name__ == "__main__":
    address = '207 N. Defiance St, Archbold, OH'
    get_geocode_3(address)
    # print(Geocoder.geocode(address)[0].coordinates)
    # get_geocode(address)
