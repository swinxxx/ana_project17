from django.conf.urls import url, include
from .views import DetailList, CustomList

urlpatterns = [
    url(r'^getall/', DetailList.as_view(), name='details'),
    url(r'^getfew/', CustomList.as_view(), name='custom'),

]

