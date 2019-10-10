# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:46:18 2017

@author: Tom Mori
"""

import csv

class sport():
     
    
    def __init__(self, team_image_path, team_schedule_path):
        self.team_logo = ImageTk.PhotoImage(Image.open(team_image_path))
#        self.team_schedule = 
    
        
#        self.ut_image = tk.Label(image=ut_image, borderwidth=0)
#        self.ut_image.place(x=(sports_x + 0),y=(sports_y + 0))
#        self.ut_image.image = ut_image

file = open('red_sox_schedule.csv', mode='r')