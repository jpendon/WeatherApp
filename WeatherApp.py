import json
import requests
import tkinter


def kelvin_to_f(k_temp):
    k_temp = float(k_temp)
    f_temp = float('%.2f' % ((k_temp - 273) * 1.8 + 32))
    return str(f_temp)


def api_url_generator(location):
    global api_url

    location = user_input.get()

    """
        ENTER API KEY 
    """
    api_key = ""

    """
        ENTER API KEY
    """
    api_url_base = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=".format(location)
    api_url = "{0}{1}".format(api_url_base, api_key)

    response = requests.get(api_url)
    json_data = json.loads(response.content.decode('utf-8'))

    city_label = tkinter.Label(mainWindow, text=location, background='grey')
    city_label.grid(row=10, column=2)

    avg_temperature(kelvin_to_f(str(json_data['main']['temp'])))
    min_temperature(kelvin_to_f(str(json_data['main']['temp_min'])))
    max_temperature(kelvin_to_f(str(json_data['main']['temp_max'])))

    weather_string = str(json_data['weather'][0])
    weather_string = weather_string[1:-1]
    weather_dict = weather_string.split(', ')

    description((weather_dict[2])[16:-1])

    wind_information(json_data['wind'])
    cloud_information(json_data['clouds']['all'])


def avg_temperature(avg_temp):
    avg_temperature_response = 'Average Temp: {} F'. format(avg_temp)

    avg_temperature_label = tkinter.Label(mainWindow, text=avg_temperature_response, background='grey')
    avg_temperature_label.grid(row=14, column=2)


def min_temperature(min_temp):
    min_temperature_response = 'Temperature Low: {} F'. format(min_temp)

    min_temperature_label = tkinter.Label(mainWindow, text=min_temperature_response, background='grey')
    min_temperature_label.grid(row=15, column=2)


def max_temperature(max_temp):
    max_temperature_response = 'Temperature High: {} F'.format(max_temp)

    max_temperature_label = tkinter.Label(mainWindow, text=max_temperature_response, background='grey')
    max_temperature_label.grid(row=16, column=2)


def description(phrase):
    phrase_label = tkinter.Label(mainWindow, text=phrase,background='grey')
    phrase_label.grid(row=17, column=2)


def wind_information(data):
    wind_speed = data['speed']
    gust_speed = data['gust']

    wind_speed_label = tkinter.Label(mainWindow, text='Wind Speed: {} m/s'.format(wind_speed), background='grey')
    wind_speed_label.grid(row=18, column=2)

    gust_speed_label = tkinter.Label(mainWindow, text='Gust Speed: {} m/s'.format(gust_speed), background='grey')
    gust_speed_label.grid(row=19, column=2)


def cloud_information(cloud_percentage):
    cloud_percentage_label = tkinter.Label(mainWindow, text='Clouds:{}%'.format(cloud_percentage), background='grey')
    cloud_percentage_label.grid(row=20, column=2)


mainWindow = tkinter.Tk()

api_url = ""

mainWindow.title("Weather Forecast")
mainWindow.geometry("430x250")
mainWindow.configure(background="grey")

city_prompt = "Enter the name of the city and Country (City, Country): "
city_prompt_label = tkinter.Label(mainWindow, text=city_prompt, background='grey')
city_prompt_label.grid(row=0, column=1, columnspan=2, )

user_input = tkinter.StringVar(mainWindow)
city_input_label = tkinter.Entry(mainWindow, textvariable=user_input)
city_input_label.bind('<Return>', api_url_generator)
city_input_label.grid(row=0, column=3, columnspan=1)


mainWindow.mainloop()
