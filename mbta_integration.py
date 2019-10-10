# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 13:39:41 2017

@author: Tom Mori
"""

from urllib import request as req
import json
import math

mbta_url = 'http://realtime.mbta.com/developer/api/v2/predictionsbystop?api_key=wX9NwuHnZU2ToO7GmGR9uw&stop=place-{0}&format=json&direction={1}&route=Green-{2}'

class mbta_train():
        
    def load_mbta_data(self):
        http_data = req.urlopen(self.url)
        json_string = http_data.read()
        json_parsed = json.loads(json_string)
        return json_parsed
    
    def get_pre_away(self):
        return int(self.train_data['mode'][0]['route'][0]['direction'][0]['trip'][0]['pre_away'])
    
    def next_trips(self):
        try:
            trip_data = []
            for trip in self.train_data['mode'][0]['route'][0]['direction'][0]['trip']:
                trip_data.append(math.floor(int(trip['pre_away'])/60))
            trip_data.sort()
            return trip_data
        except:
            return []
    
    def next_trip_text(self, index):
        trip_data = self.next_trips()
        try:
            return "{0} min".format(trip_data[index])
        except:
            return "--"

    
    def __init__(self, stop, direction, line):
        self.url = mbta_url.format(stop, direction, line)
        self.train_data = self.load_mbta_data()
        
        