from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    type = models.CharField(max_length=7, choices=[
        ('putin', 'Putin'),
        ('pullout', 'Pullout'),
        ('both', 'Both')],
        default='both')
    # photos


class Rating(models.Model):
    comment = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
