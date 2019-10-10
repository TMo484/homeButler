# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 20:24:54 2017

@author: Tom Mori
"""

import ouimeaux.environment as wemo_env
from PIL import Image as img

try:
    env = wemo_env.Environment()
    env.start()
    env.discover(seconds=10)
except OSError:
    print ("Environment already started")

class wemo_switch():
        
    def switch_on(self):
        self.switch.on()
    
    def switch_off(self):
        self.switch.off()
        
    def toggle_switch(self):
        self.switch.toggle()

    def __init__(self, switch_name):
        self.name = switch_name
        self.switch = env.get_switch(switch_name)
        self.current_state = self.switch._state
        
#    def get_button_image(self):
#        return img.open("C:\\Users\Tom Mori\Documents\Python Projects\light_bulb.jpg")
        