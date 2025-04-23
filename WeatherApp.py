__author__ = 'Jeff Werner'

import requests
import tkinter as tk
import json
import KeyValuePanel
#api key from weatherapi.com: 

root = tk.Tk()
root.title("Weather testing")
root.geometry("500x500")
root.config(bg="white")

baseUrl = "https://api.weatherapi.com/v1"
API_Key = {enter your key here}
location_var = tk.StringVar()


def displayWeatherInfo(request_data):
    result = json.loads(request_data)
    print(result["current"]["temp_f"])
    location = result["location"]["name"]
    KeyValuePanel.KeyValuePanel(root,"Location", location,100,50)
    temp_f = result["current"]["temp_f"]
    KeyValuePanel.KeyValuePanel(root, "Temp (F)",temp_f,100,100)
    wind_mph = result["current"]["wind_mph"]
    KeyValuePanel.KeyValuePanel(root, "Wind Speed", wind_mph, 100, 150)
    conditions_stat = result["current"]["condition"]["text"]
    KeyValuePanel.KeyValuePanel(root, "Condition", conditions_stat, 100, 200)
    precipitation_stat = result["current"]["precip_in"]
    KeyValuePanel.KeyValuePanel(root, "Precipitation", precipitation_stat, 100, 250)
    humitity_stat = result["current"]["humidity"]
    KeyValuePanel.KeyValuePanel(root, "Humidity", humitity_stat, 100, 300)


def makeRequest():
    weather_request = baseUrl + "/current.json"
    location_payload = {'q':location_var.get(), 'key': API_Key}
    req = requests.get(weather_request, params=location_payload)
    displayWeatherInfo(req.text)
    print(req.text)


textInput = tk.Entry(root, textvariable=location_var)
textInput.pack()
submit = tk.Button(root, text="Submit", command=makeRequest)
submit.place(x=300, y=310)
submit.pack()
root.mainloop()

