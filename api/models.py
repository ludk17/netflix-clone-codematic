from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255, null=True)
    poster = models.ImageField(upload_to='posters', null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name
