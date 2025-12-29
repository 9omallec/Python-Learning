import requests
from datetime import datetime

def search():
    key = '5caf82e12c0ed9e242007f19897b1b89'
    while True:
        city = input("What city would you like to look up? ")
        url = (f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=imperial")
        response = requests.get(url)
        if response.ok:
            data = response.json()
            print(f"City:       {data['name'].title()}")
            print(f"Clouds:     {data['weather'][0]['description'].capitalize()}")
            print(f"Temp:       {data['main']['temp']}°F")
            print(f" Min:       {data['main']['temp_min']}°F")
            print(f" Max:       {data['main']['temp_max']}°F")
            print(f"Feels Like: {data['main']['feels_like']}°F")
            print(f"Humidity:   {data['main']['humidity']}%")
            print(f"Wind:       {data['wind']['speed']} mph")
            f_url = (f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&units=imperial")
            f_response = requests.get(f_url)
            if f_response.ok:
                f_data = f_response.json()
                print("Forecast: ")
                for i in [0, 1, 2, 7]:
                    temp = f_data['list'][i]['main']['temp']
                    timestamp = f_data['list'][i]['dt']
                    date = datetime.fromtimestamp(timestamp)
                    print(f" {date.strftime('%A %I:%M %p')} - {temp}°F")
            break
        else:
            print("City Not Found!\nTry Again.")



search()
