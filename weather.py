import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
city=input("enter the name of the city: ")
url=f"https://api.weatherapi.com/v1/current.json?key=19912d981fb542f1a9b144959230604&q={city}"
r=requests.get(url)
# print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
print(f"the current temperature in {city} is {w}°C")
speak.Speak(f"the current temperature in {city} is {w} degree celcius")
