from rest_framework import serializers
from .models import TweetModel, FinalModel


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = ('date', 'place', 'tweet')
        print('HereSerial')



class FinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalModel
        fields = ('tweet', 'nature', 'disease', 'place')
        print('HereSerial')
