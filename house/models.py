import datetime
from django.db import models

# Create your models here.
class Houses(models.Model):
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    num_bed = models.IntegerField()
    year_built = models.IntegerField(('year'), choices = YEAR_CHOICES, default=datetime.datetime.now().year)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    num_room = models.IntegerField()
    num_bath = models.IntegerField()
    living_area = models.FloatField()
    property_type = models.IntegerField()
    num_parking = models.IntegerField()
    accessible_buildings = models.IntegerField()
    family_quality = models.IntegerField()
    art_expos = models.IntegerField()
    emergency_shelters = models.IntegerField()
    emergency_water = models.IntegerField()
    Facilities = models.IntegerField()
    fire_stations = models.IntegerField()
    Cultural = models.IntegerField()
    Monuments = models.IntegerField()
    police_stations = models.IntegerField()
    Vacant = models.IntegerField()
    Free_Parking = models.IntegerField()
    askprice = models.IntegerField()
