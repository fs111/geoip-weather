#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

IP_URL = 'http://ip.telize.com/'

GEOIP_URL = 'http://freegeoip.net/json/%s'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s'

KELVIN_CONSTANT = 273.15


def main():

    ipresponse = requests.get(IP_URL)
    ip = ipresponse.text
    ip = ip.strip()

    geoip_response = requests.get(GEOIP_URL % (ip))
    geoip_info = geoip_response.json()
    city, country_code = geoip_info['city'], geoip_info['country_code']

    weather_response = requests.get(WEATHER_URL % (city, country_code))
    weather_info = weather_response.json()
    
    temp = weather_info['main']['temp'] - KELVIN_CONSTANT

    print "%s(%s): %3.1fC " % (city, country_code, temp)

if __name__ == '__main__':
    main()
