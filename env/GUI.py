import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


# Function to get weather information from WeatherAPI.com

def get_weather(city, response=None):
    API_Key = '1479be5ef5c043fc857140638231810'
    url = f"http://api.weatherapi.com/v1/forecast.json?Key={API_Key}&q={city}&days=2&aqi=no&alerts=no"
    response = requests.get(url)

    if response.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    # Parse the response JSON to get weather information
    weather = response.json()

    #print(json.dumps(weather, indent=2))

    icon_id = weather['current']['condition']['icon']
    temperature = weather['current']['temp_c']
    description = weather['current']['condition']['text']
    city = weather['location']['name']
    country = weather['location']['country']
    humidity = weather['current']['humidity']
    wind = weather['current']['wind_kph']
    uv = weather['current']['uv']
    forecast_date = weather['forecast']['forecastday'][0]['date']
    max_temp = weather['forecast']['forecastday'][0]['day']['maxtemp_c']
    min_temp = weather['forecast']['forecastday'][0]['day']['mintemp_c']
    avg_temp = weather['forecast']['forecastday'][0]['day']['avgtemp_c']

    # Get the icon URL and return all the weather information
    icon_url = f"https://openweathermap.org/img/wn/10d@2x.png"
    return (icon_url, temperature, description, city, country, humidity, wind, uv, max_temp, min_temp, avg_temp, forecast_date)


# Function to search weather for a city
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # If the city is found, unpack the weather information
    icon_url, temperature, description, city, country, humidity, wind, uv, max_temp, min_temp, avg_temp, forecast_date = result
    location_label.configure(text=f"{city}, {country}")

    # Get the weather icon image from the URL and update the icon label
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Update the temperature and description labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f} °C")
    description_label.configure(text=f"Description: {description}")
    maxtemp_label.configure(text=f"Max Temperature: {max_temp:.2f} °C")
    mintemp_label.configure(text=f"Min Temperature: {min_temp:.2f} °C")
    avgtemp_label.configure(text=f"Avg Temperature: {avg_temp:.2f} °C")
    forecastdate_label.configure(text=f"Date: {forecast_date}")

    # Update the humidity, wind_label, uv
    humidity_label.configure(text=f"Humidity: {humidity}")
    wind_label.configure(text=f"Wind Speed: {wind:.2f} kph")
    uv_label.configure(text=f"UV: {uv} mW/m2")


root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("1000x1000")

# # Background
# bg = tk.PhotoImage(file = "image.png")
#
# # Background label
# bg_label = tk.Label(root, image=bg)
# bg_label.place(relwidth=1, relheight=1)

# Entry widget -> to enter the city name
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Button widget -> to search for the weather information
search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Label widget -> to show the city/country name
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# Label widget -> to show the weather icon
icon_label = tk.Label(root)
icon_label.pack()

# Label widget -> to show the temperature
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# Max Temperature
maxtemp_label = tk.Label(root, font="Helvetica, 20")
maxtemp_label.pack()

# Min Temperature
mintemp_label = tk.Label(root, font="Helvetica, 20")
mintemp_label.pack()

# Average Temperature
avgtemp_label = tk.Label(root, font="Helvetica, 20")
avgtemp_label.pack()


# Label widget -> to show the weather description
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

# Humidity widget -> to show the humidity
humidity_label = tk.Label(root, font="Helvetica, 20")
humidity_label.pack()

# Wind widget -> to show the wind speed in kph
wind_label = tk.Label(root, font="Helvetica, 20")
wind_label.pack()

# UV widget -> to show the uv
uv_label = tk.Label(root, font="Helvetica, 20")
uv_label.pack()

# Forecast date widget
forecastdate_label = tk.Label(root, font="Helvetica, 20")
forecastdate_label.pack()


root.mainloop()