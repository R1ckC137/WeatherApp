import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    api_key = '9f13acb04f3fdd6492b34b5b8ec7baf3'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key
    cities = City.objects.all()
    all_cities = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    try:
        for city in cities:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city.name,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
            }

            all_cities.append(city_info)
            print(all_cities)
    except KeyError as key:
        print(key)
    context = {'all_info': all_cities, 'form': form}

    return render(request, 'index.html', context)
