from django.shortcuts import render_to_response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import csv
import os
from rest_framework.response import Response
from django.http import JsonResponse
from .models import TweetModel
from .Serializers import TweetSerializer


class DetailList(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'

    def get(self, request, format=None):
        path= os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/all.csv')
        try:
            TweetModel.objects.all().delete()
        except:
            print("first time   ")
        with open(path) as f:
            reader = csv.reader(f)
            data_from_file= []
            for row in reader:
                dataa={ 'date': row[0], 'place': row[1], 'tweet': row[2]}
                serializer = TweetSerializer(data=dataa)
                if serializer.is_valid():
                    serializer.save()
        tweet_data = TweetModel.objects.all()
        serializer = TweetSerializer(tweet_data, many=True)
        mydict = [{}]
        for element in serializer.data:
            var={}
            for key, val in element.items():
                var[key] = val
            mydict.append(var)
        res= {'data': mydict}
        return Response(res)


class CustomList(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        print("*********************************************************")
        print(request.data)
        print("*********************************************************")
        try:
            print(request.data['place'])
            tweet_data = TweetModel.objects.filter(place=request.data['place'])
        except :
            print("first time   ")
            return Response({'error':'something went wrong'})
        serializer = TweetSerializer(tweet_data, many=True)
        return Response(serializer.data)