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



class Followupreport(APIView):
    def get(self, request, format=None):
               # General report details
        from datetime import date, timedelta, datetime

      
        today = date.today()
        current_month = today.month
        current_year = today.year
        
        report_month = today.month
        report_year = today.year
        health_facility_name = "Muhimbili Health Facility"
        district = " Kinondoni"
        report_preparer_name = "Maria Maro"
        approved_by = "Dr. Mabula Mabeyo"
        position = "Chief Medical Officer"
        health_facility_phone_number = "+0734589213"
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



        # Number of children with stunted growth
        stunted_growth_count = Child_visit.objects.filter(
            Q(height__lt=F('child__length_at_birth') + 10)  # Example condition
        ).count()




        # Aggregated data response
        data =  {
  "general_information": {
    "health_facility_name": health_facility_name,
    "district": district,
    "region": "Dar es Salaam",
    "month": report_month,
    "year": report_year,
    "report_preparer_name": report_preparer_name,
    "date": report_month,
    "cadre": "Nurse",
    "position": position,
    "approved_by": approved_by,
    "facility_district_region_phone_number": "071-356-7590",
    "date_report_received_at_district": today
  },
  "number_of_registered_children": {
    "vaccinated": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "unvaccinated": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "unknown_status": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "attendance_and_weight_for_age_height_for_age_ratios_under_1_year": {
    "total_attendance_age_3_months": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_height_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "height_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "attendance_and_weight_for_age_height_for_age_ratios_1_to_5_years": {
    "total_attendance_age_6_months": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_height_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "height_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "vitamin_a_supplementation_by_age": {
    "children_aged_6_months_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_under_1_year_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_1_to_5_years_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_6_months_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_under_1_year_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_1_to_5_years_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "deworming_with_mebendazole_albendazole": {
    "children_aged_1_to_5_years_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_1_to_5_years_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "feeding_of_infants_born_to_hiv_positive_mothers": {
    "infants_under_6_months_exclusively_breastfed": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "infants_under_6_months_not_exclusively_breastfed": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "pmtct_information_recipients": {
    "children_born_to_hiv_positive_mothers_children_with_heid_number": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_referred_to_ctc_for_treatment_and_care": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_given_lln": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  }
}


        return Response(data, status=status.HTTP_200_OK)


class Followupreport1(APIView):
    def get(self, request, format=None):
               # General report details
        from datetime import date, timedelta, datetime

      
        today = date.today()
        current_month = today.month
        current_year = today.year
        
        report_month = today.month
        report_year = today.year
        health_facility_name = "Muhimbili Health Facility"
        district = " Kinondoni"
        report_preparer_name = "Maria Maro"
        approved_by = "Dr. Mabula Mabeyo"
        position = "Chief Medical Officer"
        health_facility_phone_number = "+0734589213"
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



        # Number of children with stunted growth
        stunted_growth_count = Child_visit.objects.filter(
            Q(height__lt=F('child__length_at_birth') + 10)  # Example condition
        ).count()




        # Aggregated data response
        data =  {
  "general_information": {
    "health_facility_name": health_facility_name,
    "district": district,
    "region": "Dar es Salaam",
    "month": report_month,
    "year": report_year,
    "report_preparer_name": report_preparer_name,
    "date": report_month,
    "cadre": "Nurse",
    "position": position,
    "approved_by": approved_by,
    "facility_district_region_phone_number": "071-356-7590",
    "date_report_received_at_district": today
  },
  "number_of_registered_children": {
    "vaccinated": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "unvaccinated": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "unknown_status": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "attendance_and_weight_for_age_height_for_age_ratios_under_1_year": {
    "total_attendance_age_3_months": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_height_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "height_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "attendance_and_weight_for_age_height_for_age_ratios_1_to_5_years": {
    "total_attendance_age_6_months": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_height_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "height_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "vitamin_a_supplementation_by_age": {
    "children_aged_6_months_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_under_1_year_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_1_to_5_years_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_6_months_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_under_1_year_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_1_to_5_years_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "deworming_with_mebendazole_albendazole": {
    "children_aged_1_to_5_years_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_1_to_5_years_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "feeding_of_infants_born_to_hiv_positive_mothers": {
    "infants_under_6_months_exclusively_breastfed": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "infants_under_6_months_not_exclusively_breastfed": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "pmtct_information_recipients": {
    "children_born_to_hiv_positive_mothers_children_with_heid_number": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_referred_to_ctc_for_treatment_and_care": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_given_lln": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  }
}

        return Response(data, status=status.HTTP_200_OK)


class Followupreport2(APIView):
    def get(self, request, format=None):
               # General report details
        from datetime import date, timedelta, datetime

      
        today = date.today()
        current_month = today.month
        current_year = today.year
        
        report_month = today.month
        report_year = today.year
        health_facility_name = "Muhimbili Health Facility"
        district = " Kinondoni"
        report_preparer_name = "Maria Maro"
        approved_by = "Dr. Mabula Mabeyo"
        position = "Chief Medical Officer"
        health_facility_phone_number = "+0734589213"
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



        # Number of children with stunted growth
        stunted_growth_count = Child_visit.objects.filter(
            Q(height__lt=F('child__length_at_birth') + 10)  # Example condition
        ).count()




        # Aggregated data response
        data =  {
  "general_information": {
    "health_facility_name": health_facility_name,
    "district": district,
    "region": "Dar es Salaam",
    "month": report_month,
    "year": report_year,
    "report_preparer_name": report_preparer_name,
    "date": report_month,
    "cadre": "Nurse",
    "position": position,
    "approved_by": approved_by,
    "facility_district_region_phone_number": "071-356-7590",
    "date_report_received_at_district": today
  },
  "number_of_registered_children": {
    "vaccinated": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "unvaccinated": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "unknown_status": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "attendance_and_weight_for_age_height_for_age_ratios_under_1_year": {
    "total_attendance_age_3_months": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_height_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "height_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "attendance_and_weight_for_age_height_for_age_ratios_1_to_5_years": {
    "total_attendance_age_6_months": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "weight_for_height_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "height_for_age_ratio": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "vitamin_a_supplementation_by_age": {
    "children_aged_6_months_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_under_1_year_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_1_to_5_years_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_6_months_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_under_1_year_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_1_to_5_years_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "deworming_with_mebendazole_albendazole": {
    "children_aged_1_to_5_years_routine": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_aged_1_to_5_years_campaign": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "feeding_of_infants_born_to_hiv_positive_mothers": {
    "infants_under_6_months_exclusively_breastfed": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "infants_under_6_months_not_exclusively_breastfed": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  },
  "pmtct_information_recipients": {
    "children_born_to_hiv_positive_mothers_children_with_heid_number": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_referred_to_ctc_for_treatment_and_care": {
      "male": 0,
      "female": 0,
      "total": 0
    },
    "children_given_lln": {
      "male": 0,
      "female": 0,
      "total": 0
    }
  }
}


        return Response(data, status=status.HTTP_200_OK)
