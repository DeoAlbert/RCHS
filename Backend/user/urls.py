from django.urls import path
from .views import RegisterView, LoginView, HealthcareWorkerView, LogoutView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='create_healthcareworker'),
    path('login/', LoginView.as_view(), name='login_healthcareworker'),
    path('healthcareWorker/', HealthcareWorkerView.as_view(), name='healthcareworker'),
    path('log-out/', LogoutView.as_view(), name='healthcareworker'),
    
]