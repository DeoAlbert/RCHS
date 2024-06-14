
from django.db import models
from mother.models import Mother

# Create your models here.

class Child(models.Model):

    child_name = models.CharField(max_length=255)
    healthcare_centre_name = models.CharField(max_length=255)
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=255)
    child_number = models.IntegerField()
    child_gender = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    weight_at_birth = models.IntegerField()
    length_at_birth = models.IntegerField()
    birth_region = models.CharField(max_length=255)
    birth_district = models.CharField(max_length=255)
    residential_region = models.CharField(max_length=255)
    residential_district = models.CharField(max_length=255)
    maternal_health_worker = models.CharField(max_length=255)

    def __str__(self):
        return self.child_name


class Child_visit(models.Model):

# Foreign key:
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=255)


# The child must have a visit number
    visit_number = models.IntegerField()

# The child must be weighed every month.
    date = models.DateField()
    child_growth_and_development_status = models.CharField(max_length=255)
    return_date = models.DateField()

# VACCINATIONS (Write the Date Received)
    bcg_tuberculosis_injection_right_shoulder = models.CharField(max_length=255) #Bcg_tuberculosis_injection_in_the_right_shoulder
    polio = models.CharField(max_length=255) #Polio (Paralysis)_Drops/Orally
    dpt_hep_b = models.CharField(max_length=255) #DPT-Hep B(Diphtheria, Tetanus, Pertussis, and Hepatitis B) Injection in the Left Thigh
    pneumococcal = models.CharField(max_length=255) # PNEUMOCOCCAL-(Pneumonia) Injection in the Right Thigh
    rota = models.CharField(max_length=255) # ROTA- (Diarrhea) Drops Orally
    measles = models.CharField(max_length=255) # MEASLES Injection in the Right Thigh

# VITAMIN A AND DEWORMING MEDICATION (Mark where applicable month)
    vitamin_a = models.CharField(max_length=255) # VITAMIN A Drops / Orally
    deworming_medication = models.CharField(max_length=255) # DEWORMING MEDICATION Tablets - Orally

# Please mark ( ) if yes / (X) if no. Check the following when you find anything unusual and take the child to the doctor.
# basic VISIT details
    # date_same_as_before = models.DateField()
    weight_grams = models.IntegerField()  #Weight (Grams)
    height = models.IntegerField() # height (cm)
    anemia = models.CharField(max_length=255) # Anemia (Hb or palmar pallor)
    body_temperature = models.IntegerField() # Body temperature (°C)

# CHILD'S NUTRITION:
    exclusive_breastfeeding = models.CharField(max_length=255)# Exclusive breastfeeding (EBF)
    replacement_milk = models.CharField(max_length=255) # Replacement milk (RF)
    unable_to_breastfeed = models.CharField(max_length=255) # Unable to breastfeed
    child_play = models.CharField(max_length=255) # Observe the child's play. Is it less than usual?
    eyes = models.CharField(max_length=255) # Eyes - Are there any discharge?
    mouth = models.CharField(max_length=255) # Mouth - Is there a white film?
    ears = models.CharField(max_length=255) # Ears - Is there any discharge?

#Navel:
    navel_healed = models.CharField(max_length=255)
    navel_red = models.CharField(max_length=255)
    navel_discharge_odor = models.CharField(max_length=255)

#Skin:
    has_pus_filled_bumps = models.CharField(max_length=255)
    has_turned_yellow = models.CharField(max_length=255)

#Vaccinations:

    received_bcg = models.CharField(max_length=255) # Has the child received BCG?
    received_polio_0 = models.CharField(max_length=255) # Has the child received Polio 0?
    received_polio_1 = models.CharField(max_length=255) # Has the child received Polio 1?
    received_dtp_hep_hib = models.CharField(max_length=255) # Has the child received DTP-Hep-Hib?
    received_pneumococcal = models.CharField(max_length=255) # Has the child received Pneumococcal?
    received_rota = models.CharField(max_length=255) # Has the child received Rota?
    # Return_date_same_as_before = models.DateField()
    name_of_attendant = models.CharField(max_length=255) 
    attendant_title = models.CharField(max_length=255)

# Explain any other issues
    other_issues = models.CharField(max_length=255)
  
    def __str__(self):
        return str(self.visit_number)


class Consultation_Visit_Child(models.Model):
    
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=255)

    date = models.DateField()
    visit_type = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    other = models.CharField(max_length=255)
    test_results = models.CharField(max_length=255)
    additional_notes = models.CharField(max_length=255)
    #mother = models.ForeignKey(Mother, on_delete=models.CASCADE)

    def __str__(self):
        return self.visit_type

