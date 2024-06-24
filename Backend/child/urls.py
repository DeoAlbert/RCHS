from django.urls import path, include

from .views import getChildSummary, childStatistics, get_child_nutrition_recomendations

app_name = 'child'


urlpatterns = [

    path('getChildSummary/', getChildSummary, name='getChildSummary'),
    path('childStatistics/', childStatistics, name='childStatistics'),
    path('get_child_nutrition_recomendations/', get_child_nutrition_recomendations, name='get_child_nutrition_recomendations'),
 
]


