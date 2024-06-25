# urls.py
from django.urls import path
from .views import get_next_visit

app_name = 'notifications'


urlpatterns = [
    path('get_next_visit/', get_next_visit, name='get_next_visit'),
]
