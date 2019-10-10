# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:38:47 2017

@author: Tom Mori
"""


import pandas as pd
from PIL import Image
import time

red_sox_icon = 'C:\\Users\Tom Mori\Documents\Python Projects\sports_file\\red_sox_icon.png'
red_sox_schedule = 'C:\\Users\Tom Mori\Documents\Python Projects\sports_file\\red_sox_schedule.csv'

class sport():
     
    def next_game_time(self):
        return  time.strptime(time.ctime(self.next_game().game_time), '%a %b %d %X %Y')
    
    def next_game_opp(self):
        return self.next_game().opponent
    
    def next_game(self):
        next_game = self.team_schedule[((self.team_schedule['game_time']-time.time())/(24*60*60)) > 0].iloc[0,:]
        return next_game
    
    def __init__(self, team_image_path, team_schedule_path):
        self.team_logo = Image.open(team_image_path)
        self.team_schedule = pd.read_csv(team_schedule_path)
    
        
#        self.ut_image = tk.Label(image=ut_image, borderwidth=0)
#        self.ut_image.place(x=(sports_x + 0),y=(sports_y + 0))
#        self.ut_image.image = ut_image