#!/usr/bin/env python3
# Author: Leandro Batista
# E-mail: leandrobatistapereira98@gmail.com

import requests


def geocode(address):
    parameters = {'address': address, 'sensor': 'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)
    answer = response.json()
    print(answer['results'][0]['geometry']['location'])


if __name__ == '__main__':
    long_lat = input('Digite o endereco para pegar a latitude e longitude: ')
    geocode(long_lat)
