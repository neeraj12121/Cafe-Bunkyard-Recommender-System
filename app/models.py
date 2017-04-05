from __future__ import unicode_literals
from django.db import models


class UserProfile(models.Model):
    userid = models.IntegerField(default=0)
    username = models.CharField(max_length=30 , default='')
    password = models.CharField(max_length=30 , default='')

class Ratings(models.Model):
    userid = models.IntegerField(default=0)
    menuid = models.IntegerField(default=0)
    rating =  models.IntegerField(default=0)


class menu(models.Model):
    item = models.CharField(max_length=120)
    price = models.IntegerField()
    rating = models.IntegerField(max_length=10)
    user_rating = models.IntegerField(max_length=10)

class UserRating(models.Model):
    name = models.TextField
    item = models.CharField(max_length=120)
    person_rating = models.TextField()
    

    def __str__(self):
        return self.item
