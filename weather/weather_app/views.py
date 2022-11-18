from django.shortcuts import render

# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1db02d732975aa1e12465725dae8b5da'
    if request.method=="POST":
        city = request.POST.get('city')
        print(city)

        city_weather = requests.get(url.format(city)).json() #we are requesting the API data and converting the JSON to Python data types
        print(city_weather) #checking the output
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
            'humidity':city_weather['main']['humidity'],
            'wind':city_weather['wind']['speed']
        }
        print(weather)
        return render(request, 'index.html', {'weather' : weather})
    return render(request, 'index.html') #returns the index.html template

    