# -*- coding: utf-8 -*-
"""
Author: tmori
Date: 7/23/2017

Module handles the Wunderground portion
"""

from urllib import request as req
import json

url = 'http://api.wunderground.com/api/da40d9e23395a376/geolookup/conditions/q/MA/Brookline.json'


def wunder_request(url):
    http_data = req.urlopen(url)
#    http_data.close()
    return http_data

def parse_wunder_data(http_data):
    json_string = http_data.read()
    parsed_json = json.loads(json_string)
    return parsed_json

def extract_wunder_data(parsed_json, level_1, level_2):
    data_point = parsed_json[level_1][level_2]
    return data_point

http_data = wunder_request(url)
parsed_wgi_data = parse_wunder_data(http_data)