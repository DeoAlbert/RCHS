from django.db import models
from mother.models import Mother

# Create your models here.

class Child(models.Model):
    healthcare_centre_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)

    def __str__(self):
        return self.mother_name


class Child_visit(models.Model):
    Tarehe = models.DateField()
    Joto_la_Mwili = models.IntegerField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.Tarehe)
