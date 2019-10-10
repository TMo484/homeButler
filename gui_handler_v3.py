# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:43:29 2017

@author: Tom Mori
"""

import tkinter as tk
import time
import math

import wemo_integration as wemo
import wunderground_integration as wgi

from PIL import Image as img



monthOfYear = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
dayOfWeek = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

light_bulb = img.open("C:\\Users\Tom Mori\Documents\Python Projects\light_bulb.jpg")

col_bkgd = '#1B1B1E'
col_text = '#C5C8CE'

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.weather_update_counter = 300
        
        self.background = tk.Frame(master=self, bg=col_bkgd, width=800, height=1280)
        self.background.place(x=0,y=0)
        
        self.time_widgets()
        self.temp_widgets()
        self.wemo_widgets()
        self.weather_update_counter

        # Start the app updating
        self.update_app()

    def update_app(self):
        # Update the Time
        self.time_widgets()
        # Update the Weather; every 5 min (rate limited)
        if self.weather_update_counter >= 300:
            self.temp_widgets()
            self.weather_update_counter = 0
        # increment the Wunderground Counter
        self.weather_update_counter = self.weather_update_counter + 1
        # Update the app again in 1 second
        self.after(1000, self.update_app)

        
    def time_widgets(self): #The 'self' means that it is an instance of the main frame        
        time_x, time_y = 0, 50    
        ## format varaibles
        month = monthOfYear[int(time.strftime("%m"))]
        day = dayOfWeek[int(time.strftime("%w"))]
        
        date_var = time.strftime("{0}, {1} %d, %Y".format(day, month))
        time_var = time.strftime("%I:%M")
        
        ## add the time widget
        self.time_is = tk.Label(master=self, font=('Calibri', 95), text = time_var, fg=col_text, bg=col_bkgd, width=5, anchor='e')
        self.time_is.place(x=(time_x + 435), y=(time_y + 0))
        
        ## add the date widget
        self.date_is = tk.Label(master=self, font=('Calibri', 24), text = date_var, fg=col_text, bg=col_bkgd, width = 22, anchor='e')
        self.date_is.place(x=(time_x + 400), y=(time_y + 135))


    def temp_widgets(self): #Child of the mainframe
        temp_x, temp_y = 30, 250

        http_data = wgi.wunder_request(url)
        parsed_wgi_data = wgi.parse_wunder_data(http_data)
        
        ## add the current temperature label
        self.curr_temp_label = tk.Label(master=self, font=('Calibri', 80), fg=col_text, bg=col_bkgd,
                                   text=str(math.floor(wgi.extract_wunder_data(parsed_wgi_data, 'current_observation', 'temp_f'))) + '°F')
        self.curr_temp_label.place(x=(temp_x + 0), y=(temp_y + 0))
        
        ## add the current conditions label
        self.curr_temp_cond = tk.Label(master=self, font=('Calibri', 16), fg=col_text, bg=col_bkgd,
                                  text = wgi.extract_wunder_data(parsed_wgi_data, 'current_observation', 'weather'))
        self.curr_temp_cond.place(x=(temp_x + 280), y=(temp_y + 100))


    def wemo_widgets(self):
        wemo_x, wemo_y = 0, 0
        
        self.bedroom_lamp = wemo.wemo_switch('Hutch Lamp')
        
        self.bedroom_lamp_button = tk.Button(master=self, image=light_bulb, command= lambda: self.bedroom_lamp.toggle_switch())
        self.bedroom_lamp_button.place(x=(wemo_x) + 0, y=(wemo_y) + 175)

if __name__== "__main__":
    app = Application()
    app.geometry("800x1280")
    app.mainloop()