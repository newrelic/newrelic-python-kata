# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

import pywapi

def weather(request):
    locations = ["94041", "90008", "97202", "94110", "10024",
                 "02111", "60605", "23454", "32804", "75204",
                 "98112", "84102", "97219", "84043", "12345"]
    forecasts = []
    for location in locations:
        forecasts.append(pywapi.get_weather_from_yahoo(location))

    return render(request, 'weather/weather.html', {'forecasts': forecasts})
