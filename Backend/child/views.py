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
from mother.models import Mother_visit, Mother
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
               # General report details
        from datetime import date, timedelta, datetime

      
        today = date.today()
        current_month = today.month
        current_year = today.year
        
        report_month = today.month
        report_year = today.year
        health_facility_name = "Example Health Facility"
        district = "Example District"
        report_preparer_name = "Jane Doe"
        approved_by = "Dr. John Smith"
        position = "Chief Medical Officer"
        health_facility_phone_number = "+123456789"
        designation = "Healthcare Center"
        date_prepared = today
        date_received_at_district = today
        # Total number of children
        total_children = Child.objects.count()

        # Number of boys and girls
        total_mothers = Mother.objects.count()
        Healthcare_worker = Child.objects.filter(maternal_health_worker='Healthcare Worker').count()
        TBA = Child.objects.filter(maternal_health_worker='Traditional Birth Attendant (TBA)').count()
        Others = Child.objects.filter(maternal_health_worker='Others').count()
        boys_count = Child.objects.filter(child_gender='Male').count()
        girls_count = Child.objects.filter(child_gender='Female').count()


        # age_groups = [(10, 14), (15, 19), (20, 24), (25, 29), (30, 34), (35, 100)]

        # def get_age_group_data(queryset):
        #     data = {}
        #     for age_min, age_max in age_groups:
        #         count = queryset.filter(mother__mother_age__gte=age_min, mother__mother_age__lt=age_max).count()
        #         data[f'{age_min}-{age_max if age_max != 100 else "+"}'] = count
        #     return data

   
        # age_groups = [(10, 14), (15, 19), (20, 24), (25, 29), (30, 34), (35, 100)]

        # def get_age_group_data(queryset):
        #     data = {}
        #     for age_min, age_max in age_groups:
        #         count = queryset.filter(mother__mother_age__gte=age_min, mother__mother_age__lt=age_max).count()
        #         data[f'{age_min}-{age_max if age_max != 100 else "+"}'] = count
        #     return data

        # # Section 1: Client Visits
        # clients_attended_within_48_hours = get_age_group_data(
        #     Mother_visit.objects.filter(
        #         visit_date__year=current_year,
        #         visit_date__month=current_month,
        #         visit_date__lte=F('mother__date_of_birth') + timedelta(days=2)
        #     )
        # )

        # clients_attended_between_day_3_and_day_7 = get_age_group_data(
        #     Mother_visit.objects.filter(
        #         visit_date__year=current_year,
        #         visit_date__month=current_month,
        #         visit_date__gt=F('mother__date_of_birth') + timedelta(days=2),
        #         visit_date__lte=F('mother__date_of_birth') + timedelta(days=7)
        #     )
        # )

        # total_clients_attended_first_7_days = get_age_group_data(
        #     Mother_visit.objects.filter(
        #         visit_date__year=current_year,
        #         visit_date__month=current_month,
        #         visit_date__lte=F('mother__date_of_birth') + timedelta(days=7)
        #     )
        # )

        # clients_completed_all_visits = get_age_group_data(
        #     Mother_visit.objects.filter(
        #         visit_date__year=current_year,
        #         visit_date__month=current_month
        #     )
        # )

        # clients_with_severe_anemia = get_age_group_data(
        #     Mother_visit.objects.filter(
        #         visit_date__year=current_year,
        #         visit_date__month=current_month,
        #         hb_percentage__lt=8.5
        #     )
        # )

        # clients_with_complications = get_age_group_data(
        #     Mother_visit.objects.filter(
        #         visit_date__year=current_year,
        #         visit_date__month=current_month,
        #         complications_after_childbirth=True
        #     )
        # )

        # clients_with_convulsions = get_age_group_data(
        #     Mother_visit.objects.filter(
        #         visit_date__year=current_year,
        #         visit_date__month=current_month,
        #         convulsions=True
        #     )
        # )

        # clients_with_infected_stitches = get_age_group_data(
        #     Mother_visit.objects.filter(
        #         visit_date__year=current_year,
        #         visit_date__month=current_month,
        #         infected_stitches=True
        #     )
        # )

        # clients_with_fistula = get_age_group_data(
        #     Mother_visit.objects.filter(
        #         visit_date__year=current_year,
        #         visit_date__month=current_month,
        #         fistula=True
        #     )
        # )
        # Number of children with stunted growth
        stunted_growth_count = Child_visit.objects.filter(
            Q(height__lt=F('child__length_at_birth') + 10)  # Example condition
        ).count()

        #Child Feeding
        # children_data = Child.objects.all()
        # filter(child=child).filter(child_gender="Male")
        # for child in children_data:
        exclusive_breastfeeding_total = Child_visit.objects.filter(infant_nutrition='Exclusive Breastfeeding (EBF)').count()
        exclusive_breastfeeding_male=Child_visit.objects.filter(infant_nutrition='Exclusive Breastfeeding (EBF)').count()
        exclusive_breastfeeding_female=Child_visit.objects.filter(infant_nutrition='Exclusive Breastfeeding (EBF)').count()
        replacement_breastfeeding_total=Child_visit.objects.filter(infant_nutrition='Replacement Feeding (RF)').count()
        replacement_breastfeeding_male=Child_visit.objects.filter(infant_nutrition='Replacement Feeding (RF)').count()
        replacement_breastfeeding_female=Child_visit.objects.filter(infant_nutrition='Replacement Feeding (RF)').count()
        complementary_feeding_total=Child_visit.objects.filter(infant_nutrition='Complementary Feeding (CF)').count()
        complementary_feeding_male=Child_visit.objects.filter(infant_nutrition='Complementary Feeding (CF)').count()
        complementary_feeding_female=Child_visit.objects.filter(infant_nutrition='Complementary Feeding (CF)').count()

        # children_data = Child.objects.all()
        # for child in children_data:
        #     exclusive_breastfeeding_total = Child_visit.objects.filter(infant_nutrition='Exclusive Breastfeeding (EBF)').count()
        #     exclusive_breastfeeding_male=Child_visit.objects.filter(infant_nutrition='Exclusive Breastfeeding (EBF)').filter(child=child).filter(child_gender="Male").count()
        #     exclusive_breastfeeding_female=Child_visit.objects.filter(infant_nutrition='Exclusive Breastfeeding (EBF)').filter(child=child).filter(child_gender="Female").count()
        #     replacement_breastfeeding_total=Child_visit.objects.filter(infant_nutrition='Replacement Feeding (RF)').count()
        #     replacement_breastfeeding_male=Child_visit.objects.filter(infant_nutrition='Replacement Feeding (RF)').filter(child=child).filter(child_gender="Male").count()
        #     replacement_breastfeeding_female=Child_visit.objects.filter(infant_nutrition='Replacement Feeding (RF)').filter(child=child).filter(child_gender="Female").count()
        #     complementary_feeding_total=Child_visit.objects.filter(infant_nutrition='Complementary Feeding (CF)').count()
        #     complementary_feeding_male=Child_visit.objects.filter(infant_nutrition='Complementary Feeding (CF)').filter(child=child).filter(child_gender="Male").count()
        #     complementary_feeding_female=Child_visit.objects.filter(infant_nutrition='Complementary Feeding (CF)').filter(child=child).filter(child_gender="Female").count()



        # Aggregated data response
        data = {
             # extra
            'report_month': report_month,
            'report_year': report_year,
            'health_facility_name': health_facility_name,
            'district': district,
            'report_preparer_name': report_preparer_name,
            'approved_by': approved_by,
            'position': position,
            'health_facility_phone_number': health_facility_phone_number,
            'designation': designation,
            'date_prepared': date_prepared,
            'date_received_at_district': date_received_at_district,

            'Healthcare_worker':Healthcare_worker,
            'Others':Others,
            'TBA' : TBA,
            'parents': total_mothers,
            'total_children': total_children,
            'boys_count': boys_count,
            'girls_count': girls_count,
            'stunted_growth_count': stunted_growth_count,


       

  "section_1": {
    "clients_attended_within_48_hours": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "clients_attended_between_day_3_and_day_7": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "total_clients_attended_first_7_days": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "clients_completed_all_visits": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "clients_with_severe_anemia": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "clients_with_complications_after_childbirth": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "clients_experienced_convulsions": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "clients_with_infected_stitches": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "clients_with_fistula": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    }
  },
  "section_2": {
    "delivered_before_reaching_health_facility": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "delivered_by_TBA": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "delivered_at_home": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    }
  },
  "section_3": {
    "received_family_planning_advice": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "received_condoms": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "received_pills_POP": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "received_implants_Implanon": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0,
    },
    "received_implants_jadelle": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "received_iud": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "sterilization_btl": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "referred_for_family_planning": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    }
    },
    "section_4": {
    "came_for_postnatal_care_positive": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "tested_for_hiv_postnatal_care": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "found_hiv_postnatal_care": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "hiv_positive_ebf": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    },
    "hiv_positive_rf": {
      "10_14": 0,
      "15_19": 0,
      "20_24": 0,
      "25_29": 0,
      "30_34": 0,
      "35_plus": 0,
      "all_ages": 0
    }
  },
  
  "section_5": {
    "children_attended_within_48_hours": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_attended_between_day_3_and_day_7": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "total_children_attended_first_7_days": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_completed_all_visits": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "section_6": {
    "children_given_BCG": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_given_OPV_0": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_born_weighing_less_than_2.5kg_received_KMC": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_born_at_home_weighing_less_than_2.5kg": {
      "male": 0,
      "female": 0,
      "total": 0,
     },
    "children_born_at_home_started_KMC": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_with_severe_anemia": {
      "male": 0,
      "female": 0,
      "total": 0
    }
   },

             'section_7': {
                'severe_infection_t': 0,
                'severe_infection_m': 0,
                'severe_infection_f': 0,

            },
             'section_8': {
                'umblical_infection_t': 0,
                'umblical_infection': 0,
                'umblical_infection_f': 0,

            },
          
            'section_9': {
                'skin_infection_t': 0,
                'skin_infection_m': 0,
                'skin_infection_f': 0,

            },
            'section_10': {
                'jaundice_t': 0,
                'jaundice_m': 0,
                'jaundice_f': 0,

            },
            
             'section_11': {
                'newborn_deaths_t': 0,
                'newborn_deaths_m': 0,
                'newborn_deaths_f': 0,

            },
             'section_12': {
                'ARV_drugs_t': 0,
                'ARV_drugs_m': 0,
                'ARV_drugs_f': 0,

            },

            'section_13': {
                'newborns_exclusively_breastfed_t': exclusive_breastfeeding_total,
                'newborns_exclusively_breastfed_m': exclusive_breastfeeding_male,
                'newborns_exclusively_breastfed_f': exclusive_breastfeeding_female,

            },
            'section_14': {
                'newborns_replacemently_breastfed_t': replacement_breastfeeding_total,
                'newborns_replacemently_breastfed_m': replacement_breastfeeding_male,
                'newborns_replacemently_breastfed_f': replacement_breastfeeding_female,

            },
            'section_15': {
                'newborns_complementary_breastfed_t': complementary_feeding_total,
                'newborns_complementary_breastfed_m': complementary_feeding_male,
                'newborns_complementary_breastfed_f': complementary_feeding_female,

            }
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



