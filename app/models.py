from __future__ import unicode_literals
from django.db import models



class menu(models.Model):
    item = models.CharField(max_length=120)
    price = models.IntegerField()

   # def __unicode__(self):
    #    return self.item

    def __str__(self):
        return self.item
