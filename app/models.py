# -*- coding: utf-8 -*-
from django.db import models


class Operations(models.Model):
    email = models.CharField(max_length=100,primary_key=True)
    operations = models.CharField(max_length=1000)


class Participants(models.Model):
    mainorg = models.CharField(max_length=100,primary_key=True)
    participant = models.CharField(max_length=10000)



class Transcript(models.Model):
    email = models.CharField(max_length=100,primary_key=True)
    transcript = models.CharField(max_length=100000)
    audio_file = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)