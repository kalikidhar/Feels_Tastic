from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
# Create your views here.
# def main(request):
#     return HttpResponse("<i>Hey Hiii</i>")


from .serializers import RoomSerializer
from .models import Room

class RoomView(generics.CreateAPIView):
    query_set=Room.objects.all()
    serializer_class=RoomSerializer