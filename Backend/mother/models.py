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
    Height =models.CharField(max_length=255)
    partner_name=models.CharField(max_length=255)
    partner_age=models.IntegerField()
    partner_work=models.CharField(max_length=255)
    partner_education=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    Chairperson_name=models.CharField(max_length=255)
    pregnancies=models.IntegerField()
    alive_children=models.IntegerField()
    miscarrimother_ages = models.CharField(max_length=255)
    births=models.IntegerField()
    miscarrimother_age_year = models.CharField(max_length=255)
    miscarrimother_age_mother_age = models.CharField(max_length=255)

    def __str__(self):
        return self.mother_name


class Mother_visit(models.Model):
    Tarehe=models.DateField()
    Joto_la_Mwili=models.IntegerField()
    Blood_Preasure_140_100_na_zaidi=models.IntegerField()
    Hb_chini_ya_60=models.IntegerField()
    PMTCT_Lishe_ya_mtoto=models.CharField(max_length=255)
    Mtoto_ananyonya=models.CharField(max_length=255)
    Maziwa_yanatoka=models.CharField(max_length=255)
    Ameanza_kunyonya_ndani_ya_saa_moja=models.CharField(max_length=255)
    Chuchu_zina_vidonda=models.CharField(max_length=255)
    Yamejaa_sana=models.CharField(max_length=255)
    Yana_jipu=models.CharField(max_length=255)
    Chunguza_unyonyeshaji_toa_ushauri=models.CharField(max_length=255)
    Linanywea=models.CharField(max_length=255)
    Maumivu_makali=models.CharField(max_length=255)
    Mother=models.ForeignKey('Mother', on_delete=models.CASCADE)

    def __str__(self):
        return self.Tarehe

# jabjsjacb
##bsZHBSHfB