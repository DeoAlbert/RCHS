from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Mother, Mother_visit
from .serializers import MotherSerializer, MotherVisitSerializer

# Create your views here.

class MotherViewSet(viewsets.ModelViewSet):
    queryset= Mother.objects.all()
    serializer_class=MotherSerializer
    #permission_classes=[permissions.IsAuthenticated]


class MotherVisitViewSet(viewsets.ModelViewSet):
    queryset= Mother_visit.objects.all()
    serializer_class=MotherVisitSerializer
    #permission_classes=[permissions.IsAuthenticated]

    