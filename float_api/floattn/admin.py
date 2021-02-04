from django.contrib import admin
from .models import Location, Rating

admin.site.register([Location, Rating])
