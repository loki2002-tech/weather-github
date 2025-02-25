from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import os

root = Tk()
root.title("Weather API")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Function to get weather data
def getWeather():
    city = textfield.get()

    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    try:
        geolocator = Nominatim(user_agent="myWeatherApp")
        location = geolocator.geocode(city)
        
        if location is None:
            messagebox.showerror("Error", "City not found. Please enter a valid city name.")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        if result is None:
            messagebox.showerror("Error", "Could not determine the timezone.")
            return

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")

        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Fetch weather data
        api_key = "0c6bdecaf5967acbf2e523b093ff8b94"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(api_url)
        json_data = response.json()

        if json_data.get("cod") != 200:
            messagebox.showerror("Error", "Invalid city or API issue. Try again later.")
            return

        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)  # Convert Kelvin to Celsius
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        t.config(text=f"{temp}°C")
        c.config(text=f"{condition} / Feels like {temp}°C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description.capitalize())
        p.config(text=f"{pressure} hPa")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to safely load images
def load_image(filename):
    if os.path.exists(filename):
        return PhotoImage(file=filename)
    else:
        print(f"Warning: {filename} not found!")
        return None

# Search box
Search_image = load_image("search.png")
if Search_image:
    myimage = Label(image=Search_image)
    myimage.place(x=20, y=20)

textfield = Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = load_image("Copy of search_icon.png")
if Search_icon:
    myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", command=getWeather)
    myimage_icon.place(x=400, y=34)

# Logo
Logo_image = load_image("Copy of logo.png")
if Logo_image:
    myimage = Label(image=Logo_image)
    myimage.place(x=150, y=100)

# Bottom box
Frame_image = load_image("Copy of box.png")
if Frame_image:
    frame_myimage = Label(image=Frame_image)
    frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time display
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
Label(root, text="WIND", font=("helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=120, y=400)
Label(root, text="HUMIDITY", font=("helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=250, y=400)
Label(root, text="DESCRIPTION", font=("helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=430, y=400)
Label(root, text="PRESSURE", font=("helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
