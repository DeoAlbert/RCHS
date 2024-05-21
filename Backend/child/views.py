from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Child, Child_visit, Consultation_Visit_Child
from .serializers import ChildSerializer, ChildVisitSerializer, ChildConsultationVisitSerializer, ChildSummarySerializer, ChildVisitSummarySerializer

# Create your views here.

class ChildViewSet(viewsets.ModelViewSet):
    queryset= Child.objects.all()
    serializer_class=ChildSerializer
    #permission_classes=[permissions.IsAuthenticated]


class ChildVisitViewSet(viewsets.ModelViewSet):
    queryset= Child_visit.objects.all()
    serializer_class=ChildVisitSerializer
    #permission_classes=[permissions.IsAuthenticated]


class ChildConsultationVisitView(viewsets.ModelViewSet):
    queryset= Consultation_Visit_Child.objects.all()
    serializer_class=ChildConsultationVisitSerializer
    #permission_classes=[permissions.IsAuthenticated]


@api_view(['GET'])
def getChildSummary(request):
    children_data = Child.objects.all()
    children_data_Serializer = ChildSummarySerializer(children_data, many = True)
    
    # Extract weight and height from Child_visit objects
    children_visits_data = Child_visit.objects.all()
    children_visit_data_Serializer = ChildVisitSummarySerializer(children_visits_data, many = True)
    
    # Construct the response data
    response_data = {
        'children': children_data_Serializer.data,
        'children_visits': children_visit_data_Serializer.data
    }

    return Response(response_data)
