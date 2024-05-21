from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Mother, Mother_visit
from .serializers import MotherSerializer, MotherVisitSerializer, MotherSummarySerializer, MotherVisitSummarySerializer

# Create your views here.

class MotherViewSet(viewsets.ModelViewSet):
    queryset= Mother.objects.all()
    serializer_class=MotherSerializer
    #permission_classes=[permissions.IsAuthenticated]


class MotherVisitViewSet(viewsets.ModelViewSet):
    queryset= Mother_visit.objects.all()
    serializer_class=MotherVisitSerializer
    #permission_classes=[permissions.IsAuthenticated]


@api_view(['GET'])
def getMotherSummary(request):
    Mother_data = Mother.objects.all()
    Mother_data_Serializer = MotherSummarySerializer(Mother_data, many = True)
    
    # Extract weight and height from Child_visit objects
    Mother_visits_data = Mother_visit.objects.all()
    Mother_visit_data_Serializer = MotherVisitSummarySerializer(Mother_visits_data, many = True)
    
    # Construct the response data
    response_data = {
        'Mother': Mother_data_Serializer.data,
        'Mother_visits': Mother_visit_data_Serializer.data
    }

    return Response(response_data)


    