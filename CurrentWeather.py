import urllib.request, urllib.parse, urllib.error
import json
import ssl
import time

api_key = 'API_KEY'  # Enter your api key
serviceurl = 'https://api.openweathermap.org/data/2.5/weather?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
answer = True
while answer:
    city = input('Enter City: ')
    if len(city) < 1:
        break
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
        continue

    print("City : "+ js['name'])
    print("Country Code :", js['sys']['country'])
    print("Weather condition : ", js['weather'][0]['main'], ",", js['weather'][0]['description'])
    print("Temperature :", '%.3f' % (js['main']['temp'] - 273.15), u"\N{DEGREE SIGN}", "C")
    print("Temperature range :", '%.3f' % (js['main']['temp_min'] - 273.15), u"\N{DEGREE SIGN}", "C -",
          '%.3f' % (js['main']['temp_max'] - 273.15), u"\N{DEGREE SIGN}", "C")
    print("Pressure :", js['main']['pressure'], "hPa")
    print("Humidity", js['main']['humidity'], "%")
    print("Wind speed :", js['wind']['speed'], "m/s")
    sunrise = time.strftime("%D %H:%M", time.localtime(int(js['sys']['sunrise']))).split()
    sunset = time.strftime("%D %H:%M", time.localtime(int(js['sys']['sunset']))).split()
    print("Sunrise time :", sunrise[1])
    print("Sunset time :", sunset[1])
    print("Do you want to search again??", "Y/N")
    answer = input()
    answer = answer.upper()
    if answer == 'Y':
        answer = True
    else:
        answer = False
