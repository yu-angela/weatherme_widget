"""
Final Project

Name: Angela Yu

PennKey: yuangel (51993210)

Number of Hours Spent on Project: 27

"""
# Necessary Imports/Packages
# pip install emoji <- necessary for emojis to spawn later in code

import argparse
import json
import requests 
from tkinter import *
import emoji

class Weather:
    def __init__(self, city):
        """
        Constructs an instance of the Weather class.

        Attributes:
            self.key = string of the key needed to access weather data

        Args:
            city (str): name of the city being searched for
            self
        
        Returns:
            None
        """
        self.city = city

    def __str__(self):
        """
        Helpful in formatting outputs when printing during debugging. 

        Args:
            self
        
        Returns:
            formatted_lines (str): formatted data string
        """
        return f'The city name is {self.city}.'



def build_parser():
    """
    Builds an ArgumentParser with the specified parameters with one necessary argument of city name
        
    Args:
        None
        
    Returns:
        argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description = "Takes in city whose weather we want")

    parser.add_argument('city', help = "city name")

    return parser



def build_url(city_arg):
    """
    Builds the url with the required key, limit of entries, and city name input

    Args:
        city_arg (str): commandline argument that tells us what city to look for
    
    Returns:
        url (str): the url that is being sent as the API call 
    """
    key = "9ef3251bce7a50ce24e9100f7c299412" #personal user key 
    
    city_input = city_arg

    base_url = "http://api.openweathermap.org/data/2.5/weather?q="

    url = base_url+city_input+"&appid="+key

    return url



def get_weather_details(url):
    """
    Accesses all data from the url

    Args:
        url (str): the url from which we are making the data request from
    
    Returns:
        output (json): the json file with all data received from the request 
    """
    headers = {
        "user-agent": "CIS 1920 Spring 2023 Final Project by yuangel@sas.upenn.edu"
    }

    request = requests.get(url, headers = headers)

    output = request.json()

    return output



def store_weather_details(json_file):
    """
    Accesses the data we want from the overarching json file

    Args:
        json_file (json): all outputted data from get request
    
    Returns:
        weather_data (list): a list of dicts containing all of the information we want
    """
    weather_data = []

    if (json_file['cod'] == 200): #verifies successful access of data because the internal parameter 'cod' is always 200 if the city exists
        time = json_file['timezone']
        temperature = int(json_file['main']['temp']) - 273.15 #must convert from K to C
        clouds = json_file['clouds']['all']
        weather_descr = json_file['weather'][0]['description']

        weather_data.append(time)
        weather_data.append(temperature)
        weather_data.append(clouds)
        weather_data.append(weather_descr)
    else:
        print("Invalid city name. Please try again.")
        return None

    return weather_data



def build_widget(weather_data, city_name):
    """
    Builds the widget for display using collected data

    Args:
        weather_data (list): list containing needed data
        city_name (str): name of the city we are looking at
    
    Returns:
        N/A - widget pops up
    """
    # initializes the widget
    widget = Tk()
    widget.title("Weather App - Let's 'Look' Outside!")
    widget.geometry("500x500")

    tfield = Text(widget, width = 50, height = 20)

    tfield.delete("1.0", "end") #clear previous entries
    weather_icon = '' #default no emoji
    color_name = 'black' #default font color

    # widget details 
    if (weather_data != None):
        weather_display = f"\n\tYou're looking at {city_name}!\n\tThe time zone is {weather_data[0]}.\n\tIt is {round(weather_data[1], 3)}°C out.\n\tIt is {weather_data[2]}% cloudy.\n\tMore Info: {weather_data[3]}!"

        if (weather_data[2] <= 20):
            weather_icon = f'{emoji.emojize(":sun:")}'
        elif (weather_data[2] > 20 and weather_data[2] <= 40):
            weather_icon = f'{emoji.emojize(":sun_behind_small_cloud:")}'
        elif (weather_data[2] > 40 and weather_data[2] <= 60):
            weather_icon = f'{emoji.emojize(":sun_behind_cloud:")}'
        elif (weather_data[2] > 60 and weather_data[2] <= 80):
            weather_icon = f'{emoji.emojize(":sun_behind_large_cloud:")}'
        else:
            weather_icon = f'{emoji.emojize(":cloud:")}'

        if (weather_data[1] <= 0):
            color_name = 'blue4'
        elif (weather_data[1] > 0 and weather_data[1] <= 5):
            color_name = 'SteelBlue1'
        elif (weather_data[1] > 5 and weather_data[1] <= 10):
            color_name = 'cyan3'
        elif (weather_data[1] > 10 and weather_data[1] <= 15):
            color_name = 'DarkOliveGreen3'
        elif (weather_data[1] > 15 and weather_data[1] <= 20):
            color_name = 'OliveDrab4'
        elif (weather_data[1] > 20 and weather_data[1] <= 25):
            color_name = 'gold'
        elif (weather_data[1] > 25 and weather_data[1] <= 30):
            color_name = 'goldenrod1'
        elif (weather_data[1] > 30 and weather_data[1] <= 35):
            color_name = 'orange'
        elif (weather_data[1] > 35 and weather_data[1] <= 40):
            color_name = 'OrangeRed2'
        elif (weather_data[1] > 40 and weather_data[1] <= 45):
            color_name = 'tomato'
        elif (weather_data[1] > 45 and weather_data[1] <= 50):
            color_name = 'red2'
        else:
            color_name = 'red4'

    else:
        weather_display = f"\n\tYou looked up an invalid city name.\n\tPlease try again with a new input :)"

    tfield.insert(INSERT, weather_display)
    tfield.pack()
    
    input_label = Label(widget, text = 'Your City:', font = ('Gulim', 15, 'bold')).pack(pady = 15)
    city_name_reveal = Label(widget, text = weather_icon + city_name, width = 20, font = ('Gulim', 50, 'bold'), fg = color_name).pack()

    exit = Button(widget, text = "I'm Done!", command = widget.quit)
    exit.pack()

    widget.mainloop()



def main():
    """
        Layers together all previous functions to yield the final pop up widget after commandline arguments are given.

        Args:
            None
        
        Returns:
            None
        """
    parser = build_parser()

    args = parser.parse_args()

    weather = Weather(args.city)

    url = build_url(weather.city)

    json = get_weather_details(url)

    data = store_weather_details(json)

    build_widget(data, weather.city)



if __name__ == '__main__':
    main()