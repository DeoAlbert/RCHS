from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
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
    response_data = []

    for child in children_data:
        child_serializer = ChildSummarySerializer(child)
        latest_visit = Child_visit.objects.filter(child=child).order_by('-date').first()
        if latest_visit:
            visit_serializer = ChildVisitSummarySerializer(latest_visit)

            combined_data = {
                'id':child_serializer.data['id'],
                'child_name': child_serializer.data['child_name'],
                'child_gender': child_serializer.data['child_gender'],
                'mother_name': child_serializer.data['mother_name'],
                'age': child_serializer.data['age'],
                'weight_grams': visit_serializer.data['weight_grams'],
                'height': visit_serializer.data['height'],
                'date': visit_serializer.data['date'],
                'visit_number': visit_serializer.data['visit_number']

            }
            response_data.append(combined_data)
        else:
            combined_data = {
                'id':child_serializer.data['id'],
                'child_name': child_serializer.data['child_name'],
                'child_gender': child_serializer.data['child_gender'],
                'mother_name': child_serializer.data['mother_name'],
                'age': child_serializer.data['age'],
                'weight_grams': None,
                'height': None,
                'date': None,
                'visit_number': None

            }
            response_data.append(combined_data)

    return Response(response_data)
