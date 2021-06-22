import requests
from datetime import datetime

api_key='92305bf185f78257391b5a47d4309a78'
location=input("Enter the city name:")

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp'])-273.15)

weather_desc=api_data['weather'][0]['description']

hmdt=api_data['main']['humidity']

wind_spd=api_data['wind']['speed']

date_time=datetime.now().strftime("%d %b %Y | %M: %S %p")


print("------------------------------------------------")
print("Weather stats for - {} || {}".format(location.upper(),date_time))
print("------------------------------------------------")

print("Current temperature is {:.2f} deg C".format(temp_city))

print("Current weather desc:",weather_desc)

print("Current Humidity:",hmdt,'%')

print("Current Wind speed:",wind_spd,'kmph')

file1=open("text_file.txt","w")
l=["Enter the city name:",location,"\n------------------------------------------------","\nWeather stats for - {} || {}".format(location.upper(),date_time),"\n------------------------------------------------","\nCurrent temperature is {:.2f} deg C".format(temp_city),"\nCurrent weather desc:",weather_desc,"\nCurrent Humidity:{}%".format(hmdt),"\nCurrent Wind speed:{}kmph".format(wind_spd)]
file1.writelines(l)
file1.close()
