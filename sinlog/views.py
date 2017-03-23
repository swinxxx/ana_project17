from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import DetailsModel
from .Serializers import DetailsSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import parsers, renderers, status
from rest_framework.authtoken.serializers import AuthTokenSerializer

'''
class DetailList(generics.CreateAPIView):
    permission_classes=(AllowAny, )
    queryset = DetailsModel.objects.all()
    serializer_class = DetailsSerializer
'''

class DetailList(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        det = DetailsModel.objects.all()
        serializer = DetailsSerializer(det, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        print("*********************************************************")
        print(request.data)
        print("*********************************************************")
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save()
            tkn=Token.objects.create(user=serializer.instance)
            print(tkn.key)
            return Response(tkn.key, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #import pdb
    #pdb.set_trace()

class ObtainAuthToken(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    def post(self, request):
        print(request.data)
        #user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        print(user)
        serializer = AuthTokenSerializer(data=request.data)
        print('Its me')
        serializer.is_valid(raise_exception=True)
        print('Hello')
        user = serializer.validated_data['user']
        # Token.objects.filter(user=user).delete()
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return Response({'token': token.key})


class CheckView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        if not request.session.session_key:
            print('setting new')
            request.session.save()
        else:
            print('nothing new')
            print(request.session['country'])
        session = request.session.session_key
        print(session)
        print(request.META)
        #return Response({'token': request.META['HTTP_AUTHORIZATION']})
        return Response(status=status.HTTP_200_OK)

class ChooseCountryView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        print(request.data)
        request.session['country']=request.data
        print (request.session)
        return Response(status=status.HTTP_200_OK)

class Logout(APIView):
    queryset = DetailsModel.objects.all()
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
'''
class LogoutView(APIView):
    def get(self, request):
        print(request.data)
        Token.objects.filter(key=request.data.get('')).delete()
        token, created = Token.objects.get_or_create(user=user)
        print(token)
'''
'''
class LoginList(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = DetailsModel.objects.all()
    serializer_class = LoginSerializer
'''
'''
class LoginList():
    def post(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                request.session['auth'] = token.key
                return redirect('/sinlog/', request)
        return redirect('sinlog/login', request)
'''