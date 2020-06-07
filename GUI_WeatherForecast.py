import urllib.request, urllib.parse, urllib.error
import json
import ssl
import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

window = Tk()
window.configure(bg="white")
window.title("Weather forecast")
window.iconbitmap('icon.ico')
window.geometry("385x520")

myString = StringVar()
place = StringVar()
country = StringVar()
condition = StringVar()
temperature = StringVar()
tempRange = StringVar()
pressure = StringVar()
humidity = StringVar()
speed = StringVar()
rise = StringVar()
sunset = StringVar()


def weather():
    api_key = 'API_KEY'  #enter your api key
    serviceurl = 'https://api.openweathermap.org/data/2.5/weather?'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    city = myString.get()
    entry1.delete(0, 'end')
    extension = dict()
    extension['q'] = city
    extension['appid'] = api_key
    url = serviceurl + urllib.parse.urlencode(extension)
    print('Retrieving .....', url)
    try:
        urlh = urllib.request.urlopen(url, context=ctx)
        data = urlh.read().decode()
        js = json.loads(data)
    except:
        js = None

    if not js:
        print('===== Failure To Retrieve =====')
        print("==== Enter appropriate city ===")
        place.set("")
        country.set("")
        condition.set("")
        temperature.set("")
        tempRange.set("")
        pressure.set("")
        humidity.set("")
        speed.set("")
        messagebox.showinfo("Error", "Enter appropriate city")

    else:
        place.set("City : " + js['name'])
        country.set("Country Code : " + js['sys']['country'])
        condition.set("Weather condition : " + js['weather'][0]['main'] + "," + js['weather'][0]['description'])
        temperature.set("Temperature :" + '%.3f' % (js['main']['temp'] - 273.15) + u"\N{DEGREE SIGN}" + "C")
        tempRange.set("Temperature range : " + '%.3f' % (
                js['main']['temp_min'] - 273.15) + u"\N{DEGREE SIGN}" + "C - " + '%.3f' % (
                              js['main']['temp_max'] - 273.15) + u"\N{DEGREE SIGN}" + "C")
        pressure.set("Pressure : " + str(js['main']['pressure']) + "hPa")
        humidity.set("Humidity : " + str(js['main']['humidity']) + "%")
        speed.set("Wind speed : " + str(js['wind']['speed']) + "m/s")
        # sunrise = time.strftime("%D %H:%M" + time.localtime(int(js['sys']['sunrise']))).split()
        # Sunset = time.strftime("%D %H:%M" + time.localtime(int(js['sys']['sunset']))).split()
        # rise.set("Sunrise time : " + sunrise[1])
        # sunset.set("Sunset time : " + Sunset[1])


logo = ImageTk.PhotoImage(Image.open("logo.png"))
frame = Frame(window, bg="white").grid()
MyImage = Label(frame, image=logo, borderwidth=0).grid(row=0, column=0)

label1 = Label(frame, text="Enter City :", bg="white", font="Helvetica 13").grid(row=1, column=0)
entry1 = Entry(frame, textvariable=myString, width=24, font="Helvetica 13", borderwidth=2)
entry1.grid(row=1, column=1, ipady=1)
Button1 = Button(frame, text="Search", command=weather, bg="white", width=6, font="Helvetica 10").grid(row=1, column=2)

label2 = Label(frame, textvariable=place, bg="white", font="Helvetica 12 bold")
label2.grid(row=2, columnspan=3, pady=10)
label3 = Label(frame, textvariable=country, bg="white", font="Helvetica 12 bold")
label3.grid(row=3, columnspan=3, pady=10)
label4 = Label(frame, textvariable=condition, bg="white", font="Helvetica 12 bold")
label4.grid(row=4, columnspan=3, pady=10)
label5 = Label(frame, textvariable=temperature, bg="white", font="Helvetica 11 bold")
label5.grid(row=5, columnspan=3, pady=10)
label6 = Label(frame, textvariable=tempRange, bg="white", font="Helvetica 11")
label6.grid(row=6, columnspan=3, pady=10)
label7 = Label(frame, textvariable=pressure, bg="white", font="Helvetica 11")
label7.grid(row=7, columnspan=3, pady=10)
label8 = Label(frame, textvariable=humidity, bg="white", font="Helvetica 11")
label8.grid(row=8, columnspan=3, pady=10)
label9 = Label(frame, textvariable=speed, bg="white", font="Helvetica 11")
label9.grid(row=9, columnspan=3, pady=10)
# label10 = Label(frameBottom, textvariable=rise,bg="white").grid(row=9, column=1)
# label11 = Label(frameBottom, textvariable=sunset,bg="white").grid(row=10, column=1)
button_quit = Button(window, text="Exit", font="Helvetica 10", width=6, command=window.quit)
button_quit.grid(row=10, columnspan=3, padx=8, pady=8)
window.resizable(False, False)
window.mainloop()
