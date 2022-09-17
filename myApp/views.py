from django.shortcuts import render

import urllib.request
import json

def index(request):
    if request.method == "POST":
        city = str(request.POST.get("city"))
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=f943984d70b830a37d5a24e4482567d3').read()

        list_data = json.loads(source)
        data = {
            "country_code" : str(list_data['sys']['country']),
            "coordinate": str(list_data['coord']['lon']) + ','+ str(list_data['coord']['lat']),
            "temp": str(list_data['main']['temp']) + ' °C',
            "pressure": str(list_data['main']['pressure']),
            "humidity": str(list_data['main']['humidity']),
            'main': str(list_data['weather'][0]['main']),
            'description': str(list_data['weather'][0]['description']),
            'icon': list_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data={}

    return render(request,'index.html',data)