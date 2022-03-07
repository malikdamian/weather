from django.urls import path

from main.views import WeatherViewSet

app_name = 'weather'

data = WeatherViewSet.as_view({
    'get': 'list',
})

trigger = WeatherViewSet.as_view({
    'post': 'create'
})

urlpatterns = [
    path('data/', data, name='list'),
    path('trigger/', trigger, name='add'),
]
