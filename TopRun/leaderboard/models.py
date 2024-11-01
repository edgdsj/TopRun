from django.db import models

class Runner(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    best_time = models.FloatField()