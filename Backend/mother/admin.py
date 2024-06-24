from django.contrib import admin

# Register your models here.
from .models import  Mother, Mother_visit

admin.site.register(Mother)
admin.site.register(Mother_visit)