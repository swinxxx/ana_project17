from django.shortcuts import render_to_response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
import csv
import os
from rest_framework.response import Response
from django.http import JsonResponse
from .models import TweetModel, FinalModel
from .Serializers import TweetSerializer, FinalSerializer


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


class LoadDbFinal(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        path= os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ana/final_file.csv')
        try:
            FinalModel.objects.all().delete()
        except:
            print("first time   ")
        with open(path) as f:
            reader = csv.reader(f)
            data_from_file= []
            for row in reader:
                dataa={ 'tweet': row[1], 'nature': row[2], 'disease': row[3], 'place': row[4]}
                serializer = FinalSerializer(data=dataa)
                if serializer.is_valid():
                    serializer.save()
        tweet_data = FinalModel.objects.all()
        serializer = FinalSerializer(tweet_data, many=True)
        mydict = [{}]
        for element in serializer.data:
            var={}
            for key, val in element.items():
                var[key] = val
            mydict.append(var)
        res= {'data': mydict}
        return Response(res)

class StateStats(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'try.html'

    def get(self, request, format=None):
        return(Response({"state":"hi"}))

    def post(self, request, format=None):
        print("*********************************************************")
        print(request.data)
        print("*********************************************************")
        try:
            print(request.data['place'])
            all_data = list(FinalModel.objects.values('disease').distinct().filter(place=request.data['place']))
            print(all_data)
        except :
            print("first time")
            return Response({'error':'not found'})
        li=[{}]
        for element in all_data:
            disease=element['disease']
            print(disease)
            positive=list(FinalModel.objects.filter(place=request.data['place']).filter(disease=disease).filter(nature='positive'))
            positives=[]
            for each1 in positive:
                var=each1.__dict__
                var1={'tweet':var['tweet']}
                positives.append(var1)
            negative=list(FinalModel.objects.filter(place=request.data['place']).filter(disease=disease).filter(nature='negative'))
            negatives = []
            for each1 in negative:
                var = each1.__dict__
                var1 = {'tweet': var['tweet']}
                negatives.append(var1)

            neutral=list(FinalModel.objects.filter(place=request.data['place']).filter(disease=disease).filter(nature='neutral'))
            neutrals = []
            for each1 in neutral:
                var = each1.__dict__
                var1 = {'tweet': var['tweet']}
                neutrals.append(var1)

            dic={'disease_name': disease, 'positive_tweets': positives, 'negative_tweets': negatives, 'neutral_tweets': neutrals, 'length_neg': len(negatives), 'length_neu': len(neutrals), 'length_pos': len(positives)}
            li.append(dic)
        li.pop(0)
        print("**************((((((((((((((((((((((((((())))))))))))))))))))))))))))))))************************")

        send_list = {"place":request.data['place'], "res": li}
        print(send_list)
        return JsonResponse(send_list)


class DiseaseStats(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'diseaseStats.html'

    def get(self, request, format=None):
        return(Response({"state":"hi"}))

    def post(self, request, format=None):
        print("*********************************************************")
        print(request.data)
        print("*********************************************************")
        try:
            print(request.data['disease'])
            all_data = list(FinalModel.objects.values('place').distinct())
            print(all_data)
        except :
            print("first time")
            return Response({'error':'not found'})
        li=[{}]
        for element in all_data:
            place=element['place']
            print(place)
            positive=list(FinalModel.objects.filter(disease=request.data['disease']).filter(place=place).filter(nature='positive'))
            positives=[]
            for each1 in positive:
                var=each1.__dict__
                var1={'tweet':var['tweet']}
                positives.append(var1)
            negative=list(FinalModel.objects.filter(disease=request.data['disease']).filter(place=place).filter(nature='negative'))
            negatives = []
            for each1 in negative:
                var = each1.__dict__
                var1 = {'tweet': var['tweet']}
                negatives.append(var1)

            neutral=list(FinalModel.objects.filter(disease=request.data['disease']).filter(place=place).filter(nature='neutral'))
            neutrals = []
            for each1 in neutral:
                var = each1.__dict__
                var1 = {'tweet': var['tweet']}
                neutrals.append(var1)

            dic={'place_name': place, 'positive_tweets': positives, 'negative_tweets': negatives, 'neutral_tweets': neutrals, 'length_neg': len(negatives), 'length_neu': len(neutrals), 'length_pos': len(positives)}
            li.append(dic)
        li.pop(0)
        print(li)
        send_list = {"disease": request.data['disease'], "res": li}
        return JsonResponse(send_list)


class TotalStats(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        try:
            all_data = list(FinalModel.objects.values('disease').distinct())
        except :
            return Response({'error':'not found'})
        li=[{}]
        for element in all_data:
            disease=element['disease']
            print(disease)
            positive=list(FinalModel.objects.filter(disease=disease).filter(nature='positive'))
            positives=[]
            for each1 in positive:
                var=each1.__dict__
                var1={'tweet':var['tweet']}
                positives.append(var1)
            negative=list(FinalModel.objects.filter(disease=disease).filter(nature='negative'))
            negatives = []
            for each1 in negative:
                var = each1.__dict__
                var1 = {'tweet': var['tweet']}
                negatives.append(var1)

            neutral=list(FinalModel.objects.filter(disease=disease).filter(nature='neutral'))
            neutrals = []
            for each1 in neutral:
                var = each1.__dict__
                var1 = {'tweet': var['tweet']}
                neutrals.append(var1)

            dic={'disease_name': disease, 'positive_tweets': positives, 'negative_tweets': negatives, 'neutral_tweets': neutrals, 'length_neg': len(negatives), 'length_neu': len(neutrals), 'length_pos': len(positives)}
            li.append(dic)
        li.pop(0)
        print(li)
        return Response(li)
