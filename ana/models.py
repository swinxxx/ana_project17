from django.db import models

# Create your models here.
class TweetModel(models.Model):
    date = models.CharField(blank=False, max_length=60)
    place = models.CharField(blank=False, max_length=60)
    tweet = models.CharField(blank=False, max_length=300)

    def __unicode__(self):
        return self.name

class FinalModel(models.Model):
    place = models.CharField(blank=False, max_length=60)
    tweet = models.CharField(blank=False, max_length=300)
    disease= models.CharField(blank=False, max_length=300)
    nature = models.CharField(blank=False, max_length=300)

    def __unicode__(self):
        return self.name