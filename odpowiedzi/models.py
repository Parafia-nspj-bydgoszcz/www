# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink
import datetime

# Create your models here.

class Pytanie(models.Model):
    pytanie = models.TextField(verbose_name="pytanie")
    odpowiedz = models.TextField(verbose_name="odpowiedź")
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Odnośnik')
    timestamp = models.DateTimeField(verbose_name="data publikacji", auto_now_add=True)
#    menu = models.CharField(max_length=120, verbose_name="element menu")
#    indeks = models.PositiveSmallIntegerField(verbose_name="pozycja w menu")
    hidden = models.BooleanField(verbose_name="ukryty")

    class Meta:
        verbose_name_plural = "Ksiądz Proboszcz odpowiada" 
        ordering = ['-timestamp']
    def __unicode__(self):
        return self.pytanie
    def get_absolute_url(self):
        return '/resp/' + self.slug + '/'




    
   
