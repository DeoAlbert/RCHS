from django.urls import path, include

from .views import getMotherSummary

app_name = 'mother'


urlpatterns = [

    path('getMotherSummary/', getMotherSummary, name='getMotherSummary'),
  
]


