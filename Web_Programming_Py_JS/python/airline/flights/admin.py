from django.contrib import admin
from .models import Flight,AirPort,Passenger
# Register your models here.
admin.site.register(AirPort)
admin.site.register(Flight)
admin.site.register(Passenger)