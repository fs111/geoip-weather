#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quick script to show the current weather on the commandline. Based on geoip.

Author: André Kelpe <efeshundertelf@googlemail.com>
License: MIT

"""
import requests

# returns the external IP as simple text
IP_URL = 'http://ip.telize.com/'

# geoip service, which translates the IP to a location
GEOIP_URL = 'http://freegeoip.net/json/%s'

# weather service based on location
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s'

# temperatures in the weather service are stored in Kelvin, in order to get 
# Celcius, we have to substract this costant.
# see here: http://bugs.openweathermap.org/projects/api/wiki/Weather_Data
KELVIN_CONSTANT = 273.15


SYMBOLS = { 
           "Clouds" : u"\u2601" * 3,
           "Rain"  : u"\u2614" * 3,
           "Clear"  : u"\u2600" * 3
          }

def main():
    """main method of the program"""

    ipresponse = requests.get(IP_URL)
    ip = ipresponse.text
    ip = ip.strip()

    geoip_response = requests.get(GEOIP_URL % (ip))
    geoip_info = geoip_response.json()
    city, country_code = geoip_info['city'], geoip_info['country_code']

    weather_response = requests.get(WEATHER_URL % (city, country_code))
    weather_info = weather_response.json()
    
    temp = weather_info['main']['temp'] - KELVIN_CONSTANT

    main_weather = weather_info['weather'][0]['main']
    description = weather_info['weather'][0]['description']

    symbol = SYMBOLS.get(main_weather, "")

    print "%s(%s): %s %s, %3.1fC " % (weather_info['name'], country_code, description, symbol, temp)

if __name__ == '__main__':
    main()
