from django.conf.urls import url, include
#from rest_framework.authtoken import views
from .views import ObtainAuthToken
from .views import CheckView, Logout,ChooseCountryView


from .views import DetailList

urlpatterns = [
    url(r'^signup/', DetailList.as_view(), name='list'),
    url(r'^check', CheckView.as_view(), name='check'),
    url(r'^login/', ObtainAuthToken.as_view(), name='login'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^setcont/', ChooseCountryView.as_view(), name='choosecont'),
   # url(r'^logout/', ),
]
