from django.urls import path, include

from .views import getChildSummary, childStatistics

app_name = 'child'


urlpatterns = [

    path('getChildSummary/', getChildSummary, name='getChildSummary'),
    path('childStatistics/', childStatistics, name='childStatistics'),
 
]


