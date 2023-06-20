from django.db import models

# Create your models here.
class AirPort(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return f"{self.city} ({self.code})"
class Flight(models.Model):
    origin = models.ForeignKey(AirPort,on_delete=models.CASCADE,related_name="departures")
    destination = models.ForeignKey(AirPort,on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.id} : from {self.origin} to {self.destination}!"
class Passenger(models.Model):
    first = models.CharField(max_length=64, default="")
    last = models.CharField(max_length=64, default="")
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers", default="")
    
    def __str__(self):
        return f"{self.first} {self.last}"
