from django.urls import path, include

from .views import getMotherSummary,getParentStatistics

app_name = 'mother'


urlpatterns = [

    path('getMotherSummary/', getMotherSummary, name='getMotherSummary'),
    path('getParentStatistics/', getParentStatistics, name='getParentStatistics')
 
]


