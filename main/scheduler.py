from apscheduler.schedulers.background import BackgroundScheduler
from main.views import WeatherViewSet


def start():
    scheduler = BackgroundScheduler()
    weather = WeatherViewSet()
    scheduler.add_job(weather.save_data, 'interval', minutes=1)
    scheduler.start()
