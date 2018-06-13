# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MountainAnimal(models.Model):
    name = models.CharField(max_length=100, verbose_name='Animal Name')
    visitation_frequency = models.IntegerField(verbose_name='Frequency of Visitation')

    def __str__(self):
        return "{}. {}".format(self.id, self.name)