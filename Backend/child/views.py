from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Child, Child_visit
from .serializers import ChildSerializer, ChildVisitSerializer

# Create your views here.

class ChildViewSet(viewsets.ModelViewSet):
    queryset= Child.objects.all()
    serializer_class=ChildSerializer
    #permission_classes=[permissions.IsAuthenticated]


class ChildVisitViewSet(viewsets.ModelViewSet):
    queryset= Child_visit.objects.all()
    serializer_class=ChildVisitSerializer
    #permission_classes=[permissions.IsAuthenticated]

    