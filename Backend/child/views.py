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
from datetime import date
from django.db.models import Count, Q, F
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Child, Child_visit
from cgmzscore.src.main import z_score_with_class
import json
from datetime import date



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
        child_serializer = ChildSummarySerializer(child, context={'request': request})
        latest_visit = Child_visit.objects.filter(child=child).order_by('-date').first()
        if latest_visit:
            visit_serializer = ChildVisitSummarySerializer(latest_visit,context={'request': request})

            combined_data = {
                'url':child_serializer.data['url'],
                'child-id':child_serializer.data['id'],
                'child_visit_id':visit_serializer.data['id'],
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
                'url':child_serializer.data['url'],
                'id':child_serializer.data['id'],
                'child_visit_id':None,
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


@api_view(['GET'])
def childStatistics(request):
    total_children = Child.objects.count()
    total_male_children = Child.objects.filter(child_gender__iexact='Male').count()
    total_female_children = Child.objects.filter(child_gender__iexact='Female').count()

    # Calculate average age
    today = date.today()
    children = Child.objects.all()
    
    age_sum = sum((today.year - child.date_of_birth.year) * 12 + today.month - child.date_of_birth.month for child in children)
    average_age_months = age_sum / total_children if total_children > 0 else 0
    average_age_years = average_age_months // 12
    average_age_remainder_months = average_age_months % 12

    average_age = f"{int(average_age_years)} years, {int(average_age_remainder_months)} months"

    data = {
        'total_children': total_children,
        'total_male_children': total_male_children,
        'total_female_children': total_female_children,
        'average_age': average_age,
    }

    return Response(data)



class AggregatedDataSummaryView(APIView):
    def get(self, request, format=None):
        # Total number of children
        total_children = Child.objects.count()

        # Number of boys and girls
        boys_count = Child.objects.filter(child_gender='Male').count()
        girls_count = Child.objects.filter(child_gender='Female').count()

        # Number of children with stunted growth
        stunted_growth_count = Child_visit.objects.filter(
            Q(height__lt=F('child__length_at_birth') + 10)  # Example condition
        ).count()

        # Aggregated data response
        data = {
            'total_children': total_children,
            'boys_count': boys_count,
            'girls_count': girls_count,
            'stunted_growth_count': stunted_growth_count,
        }

        return Response(data, status=status.HTTP_200_OK)


@csrf_exempt
def get_child_nutrition_recomendations(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        registration_number = data.get('registration_number')

        try:
            child = Child.objects.get(child_number=registration_number)
            latest_visit = Child_visit.objects.filter(child=child).order_by('-date').first()
            
            if not latest_visit:
                return JsonResponse({'error': 'No visits found for this child'}, status=404)

            weight = latest_visit.weight_grams  # no need to convert grams to kg
            height = latest_visit.height
            birth_date = child.date_of_birth
            visit_date = latest_visit.date
            age_in_days = (visit_date - birth_date).days
            sex = 'M' if child.child_gender.lower() == 'male' else 'F'
            
            try:
                score = z_score_with_class(weight=str(weight), muac="13.5", age_in_days=str(age_in_days), sex=sex, height=str(height))
            except Exception as e:
                if str(e) == "too short":
                    return JsonResponse({
                        'error': 'The inputs are too small to be realistic. It is either the child has a health issue or there are wrong inputs.'
                    }, status=400)
                else:
                    return JsonResponse({'error': 'An error occurred during the Z-score calculation.'}, status=500)

            # Parse the JSON string into a dictionary
            score_data = json.loads(score)

            # Access the 'class_hfa' value
            class_hfa = score_data['class_hfa'].strip().title()
            
            age_category = '0 to 6 months' if age_in_days <= 180 else \
                           '6 to 12 months' if age_in_days <= 365 else \
                           '1 to 3 years' if age_in_days <= 1095 else '3 to 5 years'
            
            classification = f"{class_hfa} && {age_category} && {sex}"
            
            response_text = {
                'Healthy && 0 to 6 months && F': "The female child is healthy and is within the first 6 months of age.",
                'Healthy && 6 to 12 months && F': "The female child is healthy and is between 6 to 12 months old.",
                'Healthy && 1 to 3 years && F': "The female child is healthy and is between 1 to 3 years old.",
                'Healthy && 3 to 5 years && F': "The female child is healthy and is between 3 to 5 years old.",
                'Healthy && 0 to 6 months && M': "The male child is healthy and is within the first 6 months of age.",
                'Healthy && 6 to 12 months && M': "The male child is healthy and is between 6 to 12 months old.",
                'Healthy && 1 to 3 years && M': "The male child is healthy and is between 1 to 3 years old.",
                'Healthy && 3 to 5 years && M': "The male child is healthy and is between 3 to 5 years old.",
                'Moderately Stunted && 0 to 6 months && F': "The female child is moderately stunted and is within the first 6 months of age.",
                'Moderately Stunted && 6 to 12 months && F': "The female child is moderately stunted and is between 6 to 12 months old.",
                'Moderately Stunted && 1 to 3 years && F': "The female child is moderately stunted and is between 1 to 3 years old.",
                'Moderately Stunted && 3 to 5 years && F': "The female child is moderately stunted and is between 3 to 5 years old.",
                'Moderately Stunted && 0 to 6 months && M': "The male child is moderately stunted and is within the first 6 months of age.",
                'Moderately Stunted && 6 to 12 months && M': "The male child is moderately stunted and is between 6 to 12 months old.",
                'Moderately Stunted && 1 to 3 years && M': "The male child is moderately stunted and is between 1 to 3 years old.",
                'Moderately Stunted && 3 to 5 years && M': "The male child is moderately stunted and is between 3 to 5 years old.",
                'Severely Stunted && 0 to 6 months && F': "The female child is severely stunted and is within the first 6 months of age.",
                'Severely Stunted && 6 to 12 months && F': "The female child is severely stunted and is between 6 to 12 months old.",
                'Severely Stunted && 1 to 3 years && F': "The female child is severely stunted and is between 1 to 3 years old.",
                'Severely Stunted && 3 to 5 years && F': "The female child is severely stunted and is between 3 to 5 years old.",
                'Severely Stunted && 0 to 6 months && M': "The male child is severely stunted and is within the first 6 months of age.",
                'Severely Stunted && 6 to 12 months && M': "The male child is severely stunted and is between 6 to 12 months old.",
                'Severely Stunted && 1 to 3 years && M': "The male child is severely stunted and is between 1 to 3 years old.",
                'Severely Stunted && 3 to 5 years && M': "The male child is severely stunted and is between 3 to 5 years old."
            }

            response_message = response_text.get(classification, "Classification not found.")
            return JsonResponse({'message': response_message})
        
        except Child.DoesNotExist:
            return JsonResponse({'error': 'Child not found'}, status=404)
        
    return JsonResponse({'error': 'Invalid request method'}, status=400)



# import logging
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Child
# from cgmzscore.src.main import z_score_with_class

# logger = logging.getLogger(__name__)

# @csrf_exempt
# def get_child_nutrition_recomendations(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             registration_number = data.get('registration_number')
            
#             child = Child.objects.get(child_number=registration_number)
#             weight = child.weight_at_birth
#             age_in_days = (date.today() - child.date_of_birth).days
#             sex = 'M' if child.child_gender == 'Male' else 'F'
#             height = child.length_at_birth

#             logger.info(f"Weight: {weight}, Age in days: {age_in_days}, Sex: {sex}, Height: {height}")

#             score = z_score_with_class(weight=str(weight), muac="13.5", age_in_days=str(age_in_days), sex=sex, height=str(height))
            
#             return JsonResponse({'z_score': score})

#         except Child.DoesNotExist:
#             return JsonResponse({'error': 'Child not found.'}, status=404)
#         except Exception as e:
#             logger.error(f"An error occurred: {e}")
#             if str(e) == "too short":
#                 return JsonResponse({'error': 'The input values are too short.'}, status=400)
#             return JsonResponse({'error': 'An error occurred while calculating the Z-score.'}, status=500)
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=405)



