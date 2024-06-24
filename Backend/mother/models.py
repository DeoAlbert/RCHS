from django.db import models
from phone_field import PhoneField
import phonenumbers
from django.core.exceptions import ValidationError

# def validate_tanzanian_phone(value):
#     try:
#         z_number = phonenumbers.parse(value, "TZ")
#         if not phonenumbers.is_valid_number(z_number):
#             raise ValidationError("Invalid phone number for Tanzania.")
#     except phonenumbers.NumberParseException:
#         raise ValidationError("Invalid phone number format.")

# Create your models here.

class Mother (models.Model):
    healthcare_centre_name= models.CharField(max_length=255)
    mother_name=models.CharField(max_length=255)
    registration_number=models.IntegerField()
    mosquito_net_voucher_number=models.IntegerField()
    mother_age=models.IntegerField()
    mother_education=models.CharField(max_length=255)
    mother_employment=models.CharField(max_length=255)
    height =models.IntegerField()
    partner_name=models.CharField(max_length=255)
    partner_age=models.IntegerField()
    partner_work=models.CharField(max_length=255)
    partner_education=models.CharField(max_length=255)
    residential_region = models.CharField(max_length=255)
    residential_district = models.CharField(max_length=255)
    Chairperson_name=models.CharField(max_length=255)
    pregnancies=models.IntegerField(null=True, blank=True)
    alive_children=models.IntegerField(null=True, blank=True)
    miscarriages = models.IntegerField(null=True, blank=True)
    births=models.IntegerField(null=True, blank=True)
    registrant_type = models.CharField(max_length=255)
    parent_type = models.CharField(max_length=255,null=True, blank=True)
    gender = models.CharField(max_length=255)
    phone = PhoneField(help_text='Contact phone number')
    # phone = PhoneField(unique=True,validators=[validate_tanzanian_phone], help_text='Contact phone number')

    def __str__(self):
        return self.mother_name



class Mother_visit(models.Model):

    #Foreign key.
    mother=models.ForeignKey('Mother', on_delete=models.CASCADE)
    mother_name = models.CharField(max_length=255)

    
    # Visit details
    visit_number = models.CharField(max_length=255)
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
    date_of_next_visit = models.DateField()
    provider_name = models.CharField(max_length=255)
    provider_title = models.CharField(max_length=255)


    def __str__(self):
        return self.visit_date

