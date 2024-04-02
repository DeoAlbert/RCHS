from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Mother, Visit
from .serializers import MotherSerializer, VisitSerializer

from django.shortcuts import render
from rest_framework import generics


# Create your views here.

# class MotherViewSet(viewsets.ModelViewSet):
#     queryset= Mother.objects.all()
#     serializer_class=MotherSerializer
#     permission_classes=[permissions.IsAuthenticated]


# class VisitViewSet(viewsets.ModelViewSet):
#     queryset= Visit.objects.all()
#     serializer_class=VisitSerializer
#     permission_classes=[permissions.IsAuthenticated]



class Mother1(generics.ListCreateAPIView):
    queryset = Mother.objects.all()
    serializer_class = MotherSerializer

class Mother2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mother.objects.all()
    serializer_class = MotherSerializer


class Visit1(generics.ListCreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

class Visit2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
