from django.urls import path
from .views import CustomHealthcareWorkerCreate

app_name = 'users'

urlpatterns = [
    path('register/', CustomHealthcareWorkerCreate.as_view(), name='create_healthcareworker'),
]