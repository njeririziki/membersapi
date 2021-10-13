from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PrincipalSerializer,DependantsSerializer
from .models import Principal,Dependants
# Create your views here.

class PrincipalViewSet(viewsets.ModelViewSet):
    queryset =Principal.objects.all()
    serializer_class= PrincipalSerializer


class DependantsViewSet(viewsets.ModelViewSet):
    queryset =Dependants.objects.all()
    serializer_class= DependantsSerializer