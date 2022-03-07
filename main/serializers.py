from rest_framework import serializers

from main.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'city', 'country',
                  'description', 'temperature',
                  'feels_like', 'pressure',
                  'humidity', 'wind', 'created']
