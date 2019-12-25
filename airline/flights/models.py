from django.db import models

#manage.py makemigrations
# py manage.py sqlmigrate flights "table #" like 0003
# py manage.py migrate
# py manage.py shell
# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
        
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def is_valid_flight(self):
        return (self.origin != self.destination) and (self.duration >= 0)

    def __str__(self):
        return f" {self.id} - {self.origin} to {self.destination}"

class Passengers(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"