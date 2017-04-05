from django.conf.urls import url, include
from .views import DetailList, CustomList, LoadDbFinal, StateStats, DiseaseStats, TotalStats

urlpatterns = [
    url(r'^getall/', DetailList.as_view(), name='details'),
    url(r'^getfew/', CustomList.as_view(), name='custom'),
    url(r'^loadDB/', LoadDbFinal.as_view(), name='loadDB'),
    url(r'^state/', StateStats.as_view(), name='stateStats'),
    url(r'^disease/', DiseaseStats.as_view(), name='diseaseStats'),
    url(r'^total/', TotalStats.as_view(), name='totalStats'),

]

