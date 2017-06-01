from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    userid = models.IntegerField(default=0)
    username = models.CharField(max_length=30 , default='')
    password = models.CharField(max_length=30 , default='')

class Menu(models.Model):
    item = models.CharField(max_length=120)
    price = models.IntegerField()

class Ratings(models.Model):
    userid = models.IntegerField(default=0)
    menuid = models.IntegerField(default=0)
    rating =  models.IntegerField(default=0)

class UserRating(models.Model):
    name = models.TextField
    item = models.CharField(max_length=120)
    person_rating = models.TextField()
    
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    host = models.CharField(max_length=200)
    port = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " at " + self.host + ":" + str(self.port)


