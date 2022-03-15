import requests

from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from main.models import Weather
from main.permissions import IsNaskUser
from main.serializers import WeatherSerializer


class WeatherViewSet(viewsets.ModelViewSet):
    """Retrieves a list of weather information"""
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()
    permission_classes = (IsNaskUser,)
    authentication_classes = (TokenAuthentication,)

    def get_weather_data(self):
        api_key = '4fca9c1a6796c9584a3843d06a9cd7a6'
        city = 'Warsaw'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

        api_weather = requests.get(url).json()

        data = {
            'city': city,
            'country': api_weather['sys']['country'],
            'description': api_weather['weather'][0]['description'],
            'temperature': api_weather['main']['temp'],
            'feels_like': api_weather['main']['feels_like'],
            'pressure': api_weather['main']['pressure'],
            'humidity': api_weather['main']['humidity'],
            'wind': api_weather['wind']['speed']

        }
        return data

    def create(self, request, *args, **kwargs):
        """Creates an object with the current weather"""
        weather_data = self.get_weather_data()
        serializer = WeatherSerializer(data=weather_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def save_data(self):
        weather_data = self.get_weather_data()
        weather = Weather(**weather_data)
        weather.save()
