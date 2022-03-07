from django.db import models


class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Weather(Timestamp):
    city = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    feels_like = models.DecimalField(max_digits=5, decimal_places=2)
    pressure = models.PositiveSmallIntegerField()
    humidity = models.PositiveSmallIntegerField()
    wind = models.DecimalField(max_digits=5, decimal_places=2)
