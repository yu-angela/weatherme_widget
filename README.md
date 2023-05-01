Name: Angela Yu
PennID: yuangel (51993210)
Number of Hours Spent on Project: 27

Project Name: WeatherMe Widget

Packages Used:
    - One non-trivial first-party module
        - json (to access online weather data)
        - argparse (for sorting arguments)
    
    - Two non-trivial third-party modules 
        - requests (to access online weather data)
        - tkinter (to generate image of weather forecast)
        - emoji (to generate emojis within the widget)

Description: 
For my project, I made an interactive program that allows you to input a city name to find out its weather. Upon entering a city or town name as a command-line argument, a widget pop-up will appear. This pop-up will show a box at the top with the timezone of the city (to verify the correct city was searched), the temperature outside in °C, description of the weather condition, the percentage of cloudiness, and some additional notes on the weather outside. Then, the city name will spawn in a color corresponding to the temperature ranging from blue to red (cold to hot). An emoji will also spawn to the left of the city name corresponding to % of cloudiness of the city. If an invalid city name is input, then an error message will spawn in the widget as well as the string that was typed. As someone who checks the weather app every night, almost religiously, I thought that this would be very fun and somewhat useful! 

I really enjoyed the Reddit homework where we scraped off of the internet, so I wanted to interact with those skills more for this project. I was very happy to see that there is a platform called Open Weather Map that I used to access the data by requesting an API Key. On a more broad level, I wanted to create a very colorful project and felt that this would be perfect for that. To add complexity to the skills acquired from the reddit.py homework, I also wanted to challenge myself by learning to navigate something brand new, so tkinter was perfect for learning to make pop-up widgets that were both functional and pretty. I had a lot of fun learning tkinter, and I hope I was able to accomplish my goal!


Installation/Running Instructions:
First, one has to install emoji onto their local device to generate needed emojis. Then, the imports at the top of the python document must also be completed. If one is using weather.py, then it may also be useful to get a personal API key. I have hardcoded my personal key into the file, but individuals can easily create their own if needed.

After that, the code is very easy to use. After openning up the weather.py file, all one needs to do is type "python weather.py ______" into their command line terminal. The blank stands for any city name that the person desires to look up. If the city name is more than one word, then the city name MUST be included in quotes or there will be parsing issues (i.e. New York City would be typed in as "New York City", not New York City or New_York_City). The search is not case sensitive, so it is up to user discretion!

If a valid city name is accessed, then a pop-up will appear as described above in the "Description" section of this file. If one wants to search a new city, then the pop-up widget MUST be closed/exited. This can be done through clicking the "X" in the corner, command quitting the pop-up, or clicking the coded quit button called "I'm Done!" From there, the user can just type into the command line terminal again to keep searching.


Description of Code Structure:
I structured this code to most intuitively follow how I thought of reconstructing the weather widget idea in my head.

First, we begin with instantiating the Weather class that holds the current instance of the city we are working with. Within this class are my two dunder function, __init__ and __str__. Both of these functions help with clarifying which city is being accessed at any given moment, especially the __str__ function that was helpful during debugging becuase it formatted the input. I then built the parser that would allow the code to take in commandline arguments, aka the function that would allow my code to be interactive in response to typed user input. 

Then, I began working with many functions that all ultimately aim to scrape relevant data from the Open Weather website. I first built the url that the data would be called from by using a base, the command-line argument, and my personal key for Open Weather. At the end of this function, a complete url is created. From there, I accessed that url and requested information that was then formatted into a json file. Now, all relevant data is stored in a json file. 

The json file then verified for proper data access. If the data is properly scraped, then I gathered the information I needed (timezone, temperature, cloudiness, and weather description). Now that all relevant information is gathered, I build the widget in the second to last function. After initializing the widget, I display the first bits of text with the primary weather information. I also sort through the level of cloudiness to generate a corresponding emoji and the outside temperature to determine the text color of the city printed later in the code. I then display the corresponding city name and emoji large and bold beneath the weather information. 

If the data was not properly accessed, then an error is printed in the terminal about the incorrect access. The widget is still initialized but with an error message in the place where the weather information would go. There is no emoji, and the font color remains black instead of taking on a color corresponding to temperature. 

Regardless of invalid or valid input, an exit button also appears in the widget for easy exit. 

Lastly, the main function compiles all of these earlier functions to run in the proper order for the widget to pop up with the correct information. 