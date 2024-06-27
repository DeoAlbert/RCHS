from django.urls import path, include

from .views import getChildSummary, childStatistics, AggregatedDataSummaryView, Analytics, AggregatedDataSummaryView1, AggregatedDataSummaryView2
from .views import getChildSummary, childStatistics, get_child_nutrition_recomendations

app_name = 'child'


urlpatterns = [

    path('getChildSummary/', getChildSummary, name='getChildSummary'),
    path('childStatistics/', childStatistics, name='childStatistics'),
    path('ReportMonthly/', AggregatedDataSummaryView.as_view(), name='aggregated-data-summary'),
    path('ReportQuartely/', AggregatedDataSummaryView1.as_view(), name='aggregated-data-summary'),
    path('ReportAnnualy/', AggregatedDataSummaryView2.as_view(), name='aggregated-data-summary'),
    path('Analytics/', Analytics.as_view(), name='aggregated-data-summary'),
    path('get_child_nutrition_recomendations/', get_child_nutrition_recomendations, name='get_child_nutrition_recomendations'),
 
]


