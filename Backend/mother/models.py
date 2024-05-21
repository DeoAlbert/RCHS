from django.db import models

# Create your models here.

class Mother (models.Model):
    healthcare_centre_name= models.CharField(max_length=255)
    mother_name=models.CharField(max_length=255)
    registration_number=models.IntegerField()
    mosquito_net_voucher_number=models.IntegerField()
    mother_age=models.IntegerField()
    mother_education=models.CharField(max_length=255)
    mother_employment=models.CharField(max_length=255)
    Height =models.IntegerField()
    partner_name=models.CharField(max_length=255)
    partner_age=models.IntegerField()
    partner_work=models.CharField(max_length=255)
    partner_education=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    Chairperson_name=models.CharField(max_length=255)
    pregnancies=models.IntegerField()
    alive_children=models.IntegerField()
    miscarriages = models.IntegerField()
    births=models.IntegerField()
    miscarriage_age = models.IntegerField()
    miscarriage_year = models.IntegerField()

    def __str__(self):
        return self.mother_name


class Mother_visit(models.Model):

    #Foreign key.
    mother=models.ForeignKey('Mother', on_delete=models.CASCADE)
    
    # Visit details
    visit_number = models.IntegerField()
    visit_date = models.DateField()

    # Section 2: Health Measurements
    body_temperature = models.IntegerField()
    blood_pressure = models.IntegerField()
    hb_percentage = models.IntegerField()
    pmtct_nutrition = models.CharField(max_length=255)

    # Section 3: Breastfeeding
    breastfeeding = models.CharField(max_length=255)
    milk_coming_out = models.CharField(max_length=255)
    breastfeeding_within_hour = models.CharField(max_length=255)
    sore_nipples = models.CharField(max_length=255)
    full_nipples = models.CharField(max_length=255)
    abscesses = models.CharField(max_length=255)
    breastfeeding_advice = models.CharField(max_length=255)

    # Section 4: Uterus
    uterus_shrinking = models.CharField(max_length=255)
    uterus_pain = models.CharField(max_length=255)

    # Section 5: Incision / Surgical wound
    incision_did_not_tear = models.CharField(max_length=255)
    incision_type = models.CharField(max_length=255)
    wound_healed = models.CharField(max_length=255)
    pus = models.CharField(max_length=255)
    wound_open = models.CharField(max_length=255)
    bad_smell = models.CharField(max_length=255)
    lochia_amount = models.CharField(max_length=255)
    lochia_color = models.CharField(max_length=255)

    # Section 6: Mental State
    mental_state = models.CharField(max_length=255)
    mental_issues = models.CharField(max_length=255)

    # Section 7: Family Planning
    advice_given = models.CharField(max_length=255)

    # Section 8: Prophylactic Medications
    ferrous_sulphate = models.BooleanField() #default=False
    folic_acid = models.BooleanField() #default=False
    tetanus_toxoid_doses = models.CharField(max_length=255)

    # Section 9: Provider Information
    pmtct_ctx = models.CharField(max_length=255)
    postpartum_medications = models.CharField(max_length=255)
    vitamin_a = models.CharField(max_length=255)
    date_of_next_visit = models.CharField(max_length=255)
    provider_name = models.CharField(max_length=255)
    provider_title = models.CharField(max_length=255)


    def __str__(self):
        return self.visit_date

