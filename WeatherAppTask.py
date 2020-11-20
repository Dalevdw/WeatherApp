import requests
from tkinter import *
from tkinter import messagebox

api_key = "7f65701f025236c354d7754c5a4e0b71"

def location():
    city = city_selection.get()
    if city == '':
        return messagebox.showerror('Error', 'Enter a City')

    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        complete_url = base_url + "appid=" + api_key + "&q=" + cityname
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":

            y = x["main"]
            current_temp = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            Label(root, text='Temperature: '+str(round(current_temp-272.15))+' degree celsius').place(x=2, y=90)
            Label(root, text='Atmospheric Pressure: '+str(current_pressure)+' hPa').place(x=2, y=120)
            Label(root, text='Humidity: '+str(current_humidiy)).place(x=2, y=150)
            Label(root, text='Description: '+str(weather_description)).place(x=2, y=180)
        else:
            return messagebox.showerror('Error', 'No City Found')

root = Tk()
root.geometry('350x300')
root.title('Weather App')
root.configure(background="teal")
city_selection = StringVar()
Label(root, text='Weather App', font='Helvetica 12 bold').grid(row=1, column=3)
Label(root, text='Enter City:').grid(row=2, column=1)
Entry(root, width=15, textvariable=city_selection).grid(row=2, column=2)
Button(root, text='Proceed', command=location).grid(row=3, column=3)

root.mainloop()
