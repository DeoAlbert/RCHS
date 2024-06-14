from django.urls import path, include

from .views import getChildSummary, childStatistics, AggregatedDataSummaryView

app_name = 'child'


urlpatterns = [

    path('getChildSummary/', getChildSummary, name='getChildSummary'),
    path('childStatistics/', childStatistics, name='childStatistics'),
    path('aggregated-data-summary/', AggregatedDataSummaryView.as_view(), name='aggregated-data-summary'),
 
]


