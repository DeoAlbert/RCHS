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


class AnalyticsMother(APIView):
    def get(self, request, format=None):
               # General report details
        parents_count = Mother.objects.filter(registrant_type='Guardian').count()
        guardians_count = Mother.objects.filter(registrant_type='Parent').count()
        total_count = parents_count + guardians_count

      
        data = {
            'Parent': parents_count,
            'Guardians': guardians_count,
            'Total': total_count,

          "age_distribution": {
                "0-1": total_count,
                "1-2": 23,
                "2-3": 334,
                "3-4": 126,
                "4-5": 234,
                }, 

             "visit_distribution": {
                "Jan": total_count,
                "Feb": 12,
                "Mar": 36,
                "Apr": 0,
                "may": 45,
                "june": 4,
                "july": 0,
                "aug": 56,
                "sept": 0,
                "oct": 78,
                "nov": 0,
                "dec": 12,
                },    
                 }
        return Response(data, status=status.HTTP_200_OK)


                 
class Analytics(APIView):
    def get(self, request, format=None):
               # General report details
        boys_count = Child.objects.filter(child_gender='Male').count()
        girls_count = Child.objects.filter(child_gender='Female').count()
        total_count = boys_count + girls_count

      
        data = {
            'Boys_count': boys_count,
            'Girls_Count': girls_count,
            'Total_Count': total_count,

          "age_distribution": {
                "0-1": total_count,
                "1-2": 23,
                "2-3": 334,
                "3-4": 126,
                "4-5": 234,
                }, 

             "visit_distribution": {
                "Jan": total_count,
                "Feb": 12,
                "Mar": 36,
                "Apr": 0,
                "may": 45,
                "june": 4,
                "july": 0,
                "augt": 56,
                "sept": 0,
                "oct": 78,
                "nov": 0,
                "dec": 12,
                },    
                 }


        return Response(data, status=status.HTTP_200_OK)




class AggregatedDataSummaryView(APIView):
    def get(self, request, format=None):
               # General report details
        from datetime import date, timedelta, datetime

      
        today = date.today()
        current_month = today.month
        current_year = today.year
        
        report_month = today.month
        report_year = today.year
        health_facility_name = "Mnazi Mmoja Hospital"
        district = "Ilala District"
        report_preparer_name = "Karen Kuboja"
        approved_by = "Dr. Dickson House"
        position = "Chief Medical Officer"
        health_facility_phone_number = "+0754445851"
        designation = "Hospital"
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



        # Number of children with stunted growth
        stunted_growth_count = Child_visit.objects.filter(
            Q(height__lt=F('child__length_at_birth') + 10)  # Example condition
        ).count()

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

class AggregatedDataSummaryView1(APIView):
    def get(self, request, format=None):
               # General report details
        from datetime import date, timedelta, datetime

      
        today = date.today()
        current_month = today.month
        current_year = today.year
        
        report_month = today.month
        report_year = today.year
        health_facility_name = "Mnazi Mmoja Hospital"
        district = "Ilala District"
        report_preparer_name = "Karen Kuboja"
        approved_by = "Dr. Dickson House"
        position = "Chief Medical Officer"
        health_facility_phone_number = "+0754445851"
        designation = "Hospital"
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



        # Number of children with stunted growth
        stunted_growth_count = Child_visit.objects.filter(
            Q(height__lt=F('child__length_at_birth') + 10)  # Example condition
        ).count()

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



class AggregatedDataSummaryView2(APIView):
    def get(self, request, format=None):
               # General report details
        from datetime import date, timedelta, datetime

      
        today = date.today()
        current_month = today.month
        current_year = today.year
        
        report_month = today.month
        report_year = today.year
        health_facility_name = "Mnazi Mmoja Hospital"
        district = "Ilala District"
        report_preparer_name = "Karen Kuboja"
        approved_by = "Dr. Dickson House"
        position = "Chief Medical Officer"
        health_facility_phone_number = "+0754445851"
        designation = "Hospital"
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



        # Number of children with stunted growth
        stunted_growth_count = Child_visit.objects.filter(
            Q(height__lt=F('child__length_at_birth') + 10)  # Example condition
        ).count()

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


