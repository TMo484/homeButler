# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:43:29 2017

@author: Tom Mori
"""

import tkinter as tk
import time
import math
import base64
from urllib.request import urlopen

import wemo_integration as wemo
import wunderground_integration_v2 as wgi
import sports_integration_v2 as sport
import mbta_integration as mbta

from PIL import Image, ImageTk



monthOfYear = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
dayOfWeek = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

light_bulb = Image.open("C:\\Users\Tom Mori\Documents\Python Projects\light_bulb.jpg")

#Red Sox Team Data Locations
red_sox_icon = "C:\\Users\Tom Mori\Documents\Python Projects\sports_file\\red_sox_icon.png"
red_sox_schedule = "C:\\Users\Tom Mori\Documents\Python Projects\sports_file\\red_sox_schedule.csv"


col_bkgd = '#1B1B1E'
col_text = '#C5C8CE'

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.time_counter = 300
        
        self.background = tk.Frame(master=self, bg=col_bkgd, width=800, height=1280)
        self.background.place(x=0,y=0)
        
        ## initialize the widget data
#        self.wunder_data = wgi.wunder()
#        self.hutch_lamp = wemo.wemo_switch('Hutch Lamp')
#        self.bedroom_lamp = wemo.wemo_switch('Bedroom')
#        self.dining_room = wemo.wemo_switch('Dining Room')
#        self.chair_lamp = wemo.wemo_switch('Chair Lamp')
        self.rs_team = sport.sport(red_sox_icon, red_sox_schedule)
        self.cool_train = mbta.mbta_train('cool', 1, 'C')
        self.brkhl_train = mbta.mbta_train('brkhl', 1, 'D')
        
        ## set up the initial widgets
        self.time_widgets()
        self.temp_widgets()
        self.wemo_widgets()
        self.sports_widgets()
        self.mbta_widgets()

        # Start the app updating
        self.update_app()

    def update_app(self):
        # Update the Time
        self.time_widgets()
        self.mbta_widgets()
        
        # Update the Weather; every 5 min (rate limited)
        if self.time_counter >= 300:
            self.temp_widgets()
            self.time_counter = 0
            
        # increment the Wunderground Counter
        self.time_counter = self.time_counter + 1
        
        # Update the app again in 1 second
        self.after(1000, self.update_app)

        
    def time_widgets(self): #The 'self' means that it is an instance of the main frame        
        time_x, time_y = 0, 10
        ## format varaibles
        month = monthOfYear[int(time.strftime("%m"))]
        day = dayOfWeek[int(time.strftime("%w"))]
        
        date_var = time.strftime("%A, %B %d, %Y")
        time_var = time.strftime("%I:%M")
        
        ## add the time widget
        self.time_is = tk.Label(master=self, font=('Calibri', 95), text = time_var, fg=col_text, bg=col_bkgd, width=5, anchor='e')
        self.time_is.place(x=(time_x + 435), y=(time_y + 0))
        
        ## add the date widget
        self.date_is = tk.Label(master=self, font=('Calibri', 24), text = date_var, fg=col_text, bg=col_bkgd, width = 22, anchor='e')
        self.date_is.place(x=(time_x + 400), y=(time_y + 135))


    def temp_widgets(self): #Child of the mainframe
        temp_x, temp_y = 30, 35
        
        ## add the current temperature label
        self.curr_temp_label = tk.Label(master=self, font=('Calibri', 80), fg=col_text, bg=col_bkgd,
                                   text=str(math.floor(self.wunder_data.extract_wunder_data('current_observation', 'temp_f'))) + '°F')
        self.curr_temp_label.place(x=(temp_x + 0), y=(temp_y + 0))
        
        ## add the current conditions label
        self.curr_temp_cond = tk.Label(master=self, font=('Calibri', 16), fg=col_text, bg=col_bkgd,
                                  text = self.wunder_data.extract_wunder_data('current_observation', 'weather'))
        self.curr_temp_cond.place(x=(temp_x + 0), y=(temp_y + 110))

        ## add the current conditions image
#        photo = ImageTk.PhotoImage(Image.open(urlopen(self.wunder_data.extract_wunder_data('current_observation','icon_url'))))
#        self.curr_temp_cond_img = tk.Label(image=photo)
#        self.curr_temp_cond_img.place(x=(temp_x + 275), y=(temp_y + 40))
#        self.curr_temp_cond_img.image = photo

    def wemo_widgets(self):
        wemo_x, wemo_y = 0, 600
        
        light_bulb = ImageTk.PhotoImage(Image.open('C:\\Users\Tom Mori\Documents\Python Projects\light_bulb_images\light_bulb.png'))
        self.hutch_lamp_button = tk.Button(master=self, height=125, width=125, borderwidth = 0, highlightthickness = 0,
                                           image=light_bulb,
                                           command= lambda: self.hutch_lamp.toggle_switch())
        self.hutch_lamp_button.image = light_bulb
        self.hutch_lamp_button.place(x=(wemo_x) + 5, y=(wemo_y) + 175)
        self.hutch_lamp_label = tk.Label(font=('Calibri', 12), fg=col_text, bg=col_bkgd,
                                         text = 'Hutch Lamp').place(x=(wemo_x) + 25, y=(wemo_y) + 310)
        
        self.bedroom_lamp_button = tk.Button(master=self, height=125, width=125, borderwidth = 0, highlightthickness = 0,
                                             image=light_bulb
                                             , command= lambda: self.bedroom_lamp.toggle_switch())
        self.bedroom_lamp_button.place(x=(wemo_x) + 210, y=(wemo_y) + 175)
        self.bedroom_lamp_button.image = light_bulb
        self.bedroom_lamp_label = tk.Label(font=('Calibri', 12), fg=col_text, bg=col_bkgd,
                                           text = 'Bedroom Lamp').place(x=(wemo_x) + 220, y=(wemo_y) + 310)
        
        self.chair_lamp_button = tk.Button(master=self, height=125, width=125, borderwidth = 0, highlightthickness = 0,
                                           image=light_bulb
                                           , command= lambda: self.chair_lamp.toggle_switch())
        self.chair_lamp_button.place(x=(wemo_x) + 430, y=(wemo_y) + 175)
        self.chair_lamp_button.image = light_bulb
        self.chair_lamp_label = tk.Label(font=('Calibri', 12), fg=col_text, bg=col_bkgd,
                                           text = 'Chair Lamp').place(x=(wemo_x) + 450, y=(wemo_y) + 310)
        

        self.dining_room_button = tk.Button(master=self, height=125, width=125, borderwidth = 0, highlightthickness = 0,
                                           image=light_bulb
                                           , command= lambda: self.dining_room.toggle_switch())
        self.dining_room_button.place(x=(wemo_x) + 645, y=(wemo_y) + 175)
        self.dining_room_button.image = light_bulb
        self.dining_room_label = tk.Label(font=('Calibri', 12), fg=col_text, bg=col_bkgd,
                                           text = 'Dining Room').place(x=(wemo_x) + 660, y=(wemo_y) + 310)


    def sports_widgets(self):
        sports_x, sports_y = 0, 400
        
        ut_image = ImageTk.PhotoImage(Image.open('C:\\Users\Tom Mori\Documents\Python Projects\sports_file\\uni_tenn.png'))
        self.ut_image = tk.Label(image=ut_image, borderwidth=0)
        self.ut_image.place(x=(sports_x + 0),y=(sports_y + 0))
        self.ut_image.image = ut_image
        
        rs_image = ImageTk.PhotoImage(self.rs_team.team_logo)
        self.rs_image = tk.Label(image=rs_image, borderwidth=0)
        self.rs_image.place(x=(sports_x + 0),y=(sports_y + 150))
        self.rs_image.image = rs_image
        self.rs_game_date = tk.Label(font=('Calibri', 16), fg=col_text, bg=col_bkgd,
                                     text = time.strftime('%A, %B %d, %Y', self.rs_team.next_game_time())).place(x=(sports_x + 135), y=(sports_y + 160))
        self.rs_game_time = tk.Label(font=('Calibri', 16), fg=col_text, bg=col_bkgd,
                                     text = time.strftime('%I:%M %p', self.rs_team.next_game_time())).place(x=(sports_x + 135), y=(sports_y + 190))
        self.rs_game_opp = tk.Label(font=('Calibri', 16), fg=col_text, bg=col_bkgd,
                                    text = "vs. {0}".format(self.rs_team.next_game_opp())).place(x=(sports_x + 135), y = (sports_y + 220))
        
    def mbta_widgets(self):
        mbta_x, mbta_y = 400, 410
        
        mbta_image = ImageTk.PhotoImage(Image.open('C:\\Users\Tom Mori\Documents\Python Projects\mbta_files\MBTA_logo.png'))
        self.mbta_logo = tk.Label(image=mbta_image, borderwidth=0)
        self.mbta_logo.place(x=(mbta_x+180), y=(mbta_y)+0)
        self.mbta_logo.image= mbta_image
        
        self.cool_pre_away_0 = tk.Label(font=('Calibri', 16), fg=col_text, bg=col_bkgd,
                                        text = (self.cool_train.next_trip_text(0))).place(x=(mbta_x + 150), y=(mbta_y + 150))
        self.cool_pre_away_1 = tk.Label(font=('Calibri', 16), fg=col_text, bg=col_bkgd,
                                        text = (self.cool_train.next_trip_text(1))).place(x=(mbta_x + 150), y=(mbta_y + 175))

        self.brkhl_pre_away_0 = tk.Label(font=('Calibri', 16), fg=col_text, bg=col_bkgd,
                                        text = (self.brkhl_train.next_trip_text(0))).place(x=(mbta_x + 260), y=(mbta_y + 150))
        self.brkhl_pre_away_2 = tk.Label(font=('Calibri', 16), fg=col_text, bg=col_bkgd,
                                        text = (self.brkhl_train.next_trip_text(1))).place(x=(mbta_x + 260), y=(mbta_y + 175))

if __name__== "__main__":
    app = Application()
    app.geometry("800x1280")
    app.mainloop()