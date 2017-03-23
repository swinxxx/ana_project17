from rest_framework import serializers
from .models import DetailsModel


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsModel
        fields = ('type', 'name', 'email', 'password','country')
        print('HereSerial')



