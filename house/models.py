from django.db import models


# Create your models here.


class Train(models.Model):
    coef_distance_to_citycenter = models.FloatField(default=0)
    coef_distance_to_airport = models.FloatField(default=0)
    coef_distance_to_station = models.FloatField(default=0)
    coef_year_built = models.FloatField(default=0)
    coef_num_room = models.FloatField(default=0)
    coef_num_bed = models.FloatField(default=0)
    coef_num_bath = models.FloatField(default=0)
    coef_living_area = models.FloatField(default=0)
    intercept = models.FloatField(default=0)
    score = models.FloatField(default=0)
    rmse = models.FloatField(default=0)
