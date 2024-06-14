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
    response_data = []

    for mother in Mother_data:
        mother_serializer = MotherSummarySerializer(mother, context={'request': request})
        latest_visit = Mother_visit.objects.filter(mother=mother).order_by('-visit_date').first()
        if latest_visit:
            visit_serializer = MotherVisitSummarySerializer(latest_visit,context={'request': request})

            combined_data = {
                'url':mother_serializer.data['url'],
                'id':mother_serializer.data['id'],
                'mother_visit_id':visit_serializer.data['id'],
                'mother_name': mother_serializer.data['mother_name'],
                'mother_age': mother_serializer.data['mother_age'],
                'partner_name': mother_serializer.data['partner_name'],
                'visit_date': visit_serializer.data['visit_date'],
                'visit_number': visit_serializer.data['visit_number']

            }
            response_data.append(combined_data)
        else:
            combined_data = {
                'url':mother_serializer.data['url'],
                'id':mother_serializer.data['id'],
                'mother_visit_id':None,
                'mother_name': mother_serializer.data['mother_name'],
                'mother_age': mother_serializer.data['mother_age'],
                'partner_name': mother_serializer.data['partner_name'],
                'visit_date': None,
                'visit_number': None

            }
            response_data.append(combined_data)

    return Response(response_data)


@api_view(['GET'])
def getParentStatistics(request):
    total_parents = Mother.objects.count()

    data = {
        'total_parents': total_parents
    }

    return Response(data)

    