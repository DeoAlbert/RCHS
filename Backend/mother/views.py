from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Mother, Visit
from .serializers import MotherSerializer, VisitSerializer

# Create your views here.

class MotherViewSet(viewsets.ModelViewSet):
    queryset= Mother.objects.all()
    serializer_class=MotherSerializer
    permission_classes=[permissions.IsAuthenticated]


class VisitViewSet(viewsets.ModelViewSet):
    queryset= Visit.objects.all()
    serializer_class=VisitSerializer
    permission_classes=[permissions.IsAuthenticated]