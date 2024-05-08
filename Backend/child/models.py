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

# The child must be weighed every month.
    Date = models.DateField()
    Child_growth_and_development_status = models.CharField(max_length=255)
    Return_date = models.DateField()

# VACCINATIONS (Write the Date Received)
    Bcg_tuberculosis_injection_right_shoulder = models.CharField(max_length=255) #Bcg_tuberculosis_injection_in_the_right_shoulder
    Polio = models.CharField(max_length=255) #Polio (Paralysis)_Drops/Orally
    Dpt_hep_b = models.CharField(max_length=255) #DPT-Hep B(Diphtheria, Tetanus, Pertussis, and Hepatitis B) Injection in the Left Thigh
    Pneumococcal = models.CharField(max_length=255) # PNEUMOCOCCAL-(Pneumonia) Injection in the Right Thigh
    Rota = models.CharField(max_length=255) # ROTA- (Diarrhea) Drops Orally
    Measles = models.CharField(max_length=255) # MEASLES Injection in the Right Thigh

# VITAMIN A AND DEWORMING MEDICATION (Mark where applicable month)
    Vitamin_a = models.CharField(max_length=255) # VITAMIN A Drops / Orally
    Deworming_medication = models.CharField(max_length=255) # DEWORMING MEDICATION Tablets - Orally

# Please mark ( ) if yes / (X) if no. Check the following when you find anything unusual and take the child to the doctor.
# basic VISIT details
    # Date_same_as_before = models.DateField()
    Weight_grams = models.IntegerField()  #Weight (Grams)
    Anemia = models.CharField(max_length=255) # Anemia (Hb or palmar pallor)
    Body_temperature = models.IntegerField() # Body temperature (°C)

# CHILD'S NUTRITION:
    Exclusive_breastfeeding = models.CharField(max_length=255)# Exclusive breastfeeding (EBF)
    Replacement_milk = models.CharField(max_length=255) # Replacement milk (RF)
    Unable_to_breastfeed = models.CharField(max_length=255) # Unable to breastfeed
    Child_play = models.CharField(max_length=255) # Observe the child's play. Is it less than usual?
    Eyes = models.CharField(max_length=255) # Eyes - Are there any discharge?
    Mouth = models.CharField(max_length=255) # Mouth - Is there a white film?
    Ears = models.CharField(max_length=255) # Ears - Is there any discharge?

#Navel:
    Navel_Healed = models.CharField(max_length=255)
    Navel_Red = models.CharField(max_length=255)
    Navel_Discharge_odor = models.CharField(max_length=255)

#Skin:
    Has_pus_filled_bumps = models.CharField(max_length=255)
    Has_turned_yellow = models.CharField(max_length=255)

#Vaccinations:

    Received_BCG = models.CharField(max_length=255) # Has the child received BCG?
    Received_Polio_0 = models.CharField(max_length=255) # Has the child received Polio 0?
    Received_Polio_1 = models.CharField(max_length=255) # Has the child received Polio 1?
    Received_DTP_Hep_Hib = models.CharField(max_length=255) # Has the child received DTP-Hep-Hib?
    Received_Pneumococcal = models.CharField(max_length=255) # Has the child received Pneumococcal?
    Received_Rota = models.CharField(max_length=255) # Has the child received Rota?
    # Return_date_same_as_before = models.DateField()
    Name_of_attendant = models.CharField(max_length=255) 
    Attendant_title = models.CharField(max_length=255)

# Explain any other issues
    Other_issues = models.CharField(max_length=255)

# Foreign key:
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.Tarehe)


class Consultation_Visit_Child(models.Model):
    Tarehe = models.DateField()
    Visit_type = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    other = models.CharField(max_length=255)
    Test_Results = models.CharField(max_length=255)
    Additional_Notes = models.CharField(max_length=255)
    #mother = models.ForeignKey(Mother, on_delete=models.CASCADE)

    def __str__(self):
        return self.child_name
