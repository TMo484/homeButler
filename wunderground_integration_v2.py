# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 20:59:59 2017

@author: Tom Mori
"""


from urllib import request as req
import json

url = 'http://api.wunderground.com/api/da40d9e23395a376/geolookup/conditions/q/MA/Brookline.json'

class wunder():

    def wunder_request(self, url):
        http_data = req.urlopen(url)
        return http_data
    
    def parse_wunder_data(self, http_data):
        json_string = http_data.read()
        parsed_json = json.loads(json_string)
        return parsed_json
    
    def extract_wunder_data(self, level_1, level_2):
        data_point = self.parsed_data[level_1][level_2]
        return data_point
    
    def __init__(self):
        self.http_data = self.wunder_request(url)
        self.parsed_data = self.parse_wunder_data(self.http_data)