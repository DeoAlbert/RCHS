from . import views
from django.urls import path


urlpatterns = [
    path("mother/", views.Mother1.as_view(), name ='blog-view'),
    path("mother2/<int:pk>/", views.Mother2.as_view(), name ='blog-view'),
    path("visit/", views.Visit1.as_view(), name ='blog-view'),
    path("visit2/<int:pk>/", views.Visit2.as_view(), name ='blog-view')
]