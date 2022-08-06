from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']

@admin.register(models.Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
