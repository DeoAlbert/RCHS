from django.urls import path, include

from .views import getChildSummary

app_name = 'child'


urlpatterns = [

    path('getChildSummary/', getChildSummary, name='getChildSummary'),
  
]


