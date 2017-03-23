from django.db import models

# Create your models here.
class TweetModel(models.Model):
    date = models.CharField(blank=False, max_length=60)
    place = models.CharField(blank=False, max_length=60)
    tweet = models.CharField(blank=False, max_length=300)