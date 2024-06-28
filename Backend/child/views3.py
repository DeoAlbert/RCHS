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
  "General Information": {
    "Health Facility Name": health_facility_name,
    "District": district,
    "Region": "Dar es Salaam",
    "Month": report_month,
    "Year": report_year,
    "Report Preparer's Name": report_preparer_name,
    "Date": report_month,
    "Cadre": "Nurse",
    "Position": position,
    "Approved by": approved_by,
    "Facility/District/Region Phone Number": "071-356-7590",
    "Date Report Received at District": today
  },
  "Number of Registered Children": {
    "Vaccinated": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Unvaccinated": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Unknown Status": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Attendance and Weight-for-Age/Height-for-Age Ratios (Under 1 Year)": {
    "Total Attendance (age 3 months)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Age Ratio (>80% or >-2SD, 60-80% or -2 to -3SD, <60% or <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Height Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Height-for-Age Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Attendance and Weight-for-Age/Height-for-Age Ratios (1 to 5 Years)": {
    "Total Attendance (age 6 months)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Age Ratio (>80% or >-2SD, 60-80% or -2 to -3SD, <60% or <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Height Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Height-for-Age Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Vitamin A Supplementation by Age": {
    "Children aged 6 months (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children under 1 year (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 1 to 5 years (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 6 months (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children under 1 year (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 1 to 5 years (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Deworming with Mebendazole/Albendazole": {
    "Children aged 1 to 5 years (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 1 to 5 years (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Feeding of Infants Born to HIV Positive Mothers": {
    "Infants under 6 months exclusively breastfed (EBF)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Infants under 6 months not exclusively breastfed (with H in EBF)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "PMTCT Information/Recipients": {
    "Children born to HIV positive mothers/children with HEID number": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children referred to CTC for treatment and care": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children given LLN": {
      "Male": 0,
      "Female": 0,
      "Total": 0
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
  "General Information": {
    "Health Facility Name": health_facility_name,
    "District": district,
    "Region": "Dar es Salaam",
    "Month": report_month,
    "Year": report_year,
    "Report Preparer's Name": report_preparer_name,
    "Date": report_month,
    "Cadre": "Nurse",
    "Position": position,
    "Approved by": approved_by,
    "Facility/District/Region Phone Number": "071-356-7590",
    "Date Report Received at District": today
  },
  "Number of Registered Children": {
    "Vaccinated": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Unvaccinated": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Unknown Status": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Attendance and Weight-for-Age/Height-for-Age Ratios (Under 1 Year)": {
    "Total Attendance (age 3 months)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Age Ratio (>80% or >-2SD, 60-80% or -2 to -3SD, <60% or <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Height Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Height-for-Age Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Attendance and Weight-for-Age/Height-for-Age Ratios (1 to 5 Years)": {
    "Total Attendance (age 6 months)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Age Ratio (>80% or >-2SD, 60-80% or -2 to -3SD, <60% or <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Height Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Height-for-Age Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Vitamin A Supplementation by Age": {
    "Children aged 6 months (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children under 1 year (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 1 to 5 years (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 6 months (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children under 1 year (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 1 to 5 years (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Deworming with Mebendazole/Albendazole": {
    "Children aged 1 to 5 years (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 1 to 5 years (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Feeding of Infants Born to HIV Positive Mothers": {
    "Infants under 6 months exclusively breastfed (EBF)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Infants under 6 months not exclusively breastfed (with H in EBF)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "PMTCT Information/Recipients": {
    "Children born to HIV positive mothers/children with HEID number": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children referred to CTC for treatment and care": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children given LLN": {
      "Male": 0,
      "Female": 0,
      "Total": 0
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
  "General Information": {
    "Health Facility Name": health_facility_name,
    "District": district,
    "Region": "Dar es Salaam",
    "Month": report_month,
    "Year": report_year,
    "Report Preparer's Name": report_preparer_name,
    "Date": report_month,
    "Cadre": "Nurse",
    "Position": position,
    "Approved by": approved_by,
    "Facility/District/Region Phone Number": "071-356-7590",
    "Date Report Received at District": today
  },
  "Number of Registered Children": {
    "Vaccinated": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Unvaccinated": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Unknown Status": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Attendance and Weight-for-Age/Height-for-Age Ratios (Under 1 Year)": {
    "Total Attendance (age 3 months)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Age Ratio (>80% or >-2SD, 60-80% or -2 to -3SD, <60% or <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Height Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Height-for-Age Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Attendance and Weight-for-Age/Height-for-Age Ratios (1 to 5 Years)": {
    "Total Attendance (age 6 months)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Age Ratio (>80% or >-2SD, 60-80% or -2 to -3SD, <60% or <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Weight-for-Height Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Height-for-Age Ratio (>-2SD, -2 to -3SD, <-3SD)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Vitamin A Supplementation by Age": {
    "Children aged 6 months (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children under 1 year (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 1 to 5 years (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 6 months (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children under 1 year (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 1 to 5 years (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Deworming with Mebendazole/Albendazole": {
    "Children aged 1 to 5 years (Routine)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children aged 1 to 5 years (Campaign)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "Feeding of Infants Born to HIV Positive Mothers": {
    "Infants under 6 months exclusively breastfed (EBF)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Infants under 6 months not exclusively breastfed (with H in EBF)": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  },
  "PMTCT Information/Recipients": {
    "Children born to HIV positive mothers/children with HEID number": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children referred to CTC for treatment and care": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    },
    "Children given LLN": {
      "Male": 0,
      "Female": 0,
      "Total": 0
    }
  }
}

        return Response(data, status=status.HTTP_200_OK)
