from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Person
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema

# Create your views here.



class CreatePersonView(generics.ListCreateAPIView):
    """
    Creating a Person object with the name attribute
    return the name of the person with a unique id    param: name-> String
    
    """
    serializer_class = CreateUserSerializers
    queryset = Person.objects.all()
    
class ReadAllView(generics.ListAPIView):
    """View all available Person's object on the data base including thier name and their ids"""
    serializer_class = CreateUserSerializers
    queryset = Person.objects.all()


class UpdatePersonView(generics.RetrieveUpdateDestroyAPIView):
    """Update,DELETE, RETREVE a Person Object name using their unique ID"""
    serializer_class = UpdatePersonSerializer
    queryset = Person.objects.all()


