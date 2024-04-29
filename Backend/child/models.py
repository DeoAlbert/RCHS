from django.db import models
from mother.models import Mother

# Create your models here.

class Child(models.Model):
    healthcare_centre_name = models.CharField(max_length=255)
    child_number = models.CharField(max_length=255)
    child_name = models.CharField(max_length=255)
    child_gender = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    weight_at_birth = models.CharField(max_length=255)
    length_at_birth = models.CharField(max_length=255)
    place_of_birth = models.CharField(max_length=255)
    maternal_health_worker = models.CharField(max_length=255)
    child_residence = models.CharField(max_length=255)
    #mother = models.ForeignKey(Mother, on_delete=models.CASCADE)

    def __str__(self):
        return self.child_name


class Child_visit(models.Model):
    Tarehe = models.DateField()
    Joto_la_Mwili = models.IntegerField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.Tarehe)
