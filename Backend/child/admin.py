from django.contrib import admin

# Register your models here.
from .models import  Child, Child_visit, Consultation_Visit_Child

admin.site.register(Consultation_Visit_Child)
admin.site.register(Child)
admin.site.register(Child_visit)