from django.db import models

# Create your models here.

class Mother (models.Model):
    healthcare_centre_name= models.CharField(max_length=255)
    Mothers_name=models.CharField(max_length=255)
    RegistrationNumber=models.IntegerField()
    MosquitoNetVoucherNumber=models.IntegerField()
    Mage=models.IntegerField()
    MEducation=models.CharField(max_length=255)
    Mwork=models.CharField(max_length=255)
    Height =models.CharField(max_length=255)
    Fathers_name=models.CharField(max_length=255)
    Fage=models.IntegerField()
    Feducation=models.CharField(max_length=255)
    Fwork=models.CharField(max_length=255)
    Village=models.CharField(max_length=255)
    ChairpersonsName=models.CharField(max_length=255)
    how_many_pregnancies=models.IntegerField()
    Alive_children=models.IntegerField()
    Miscarriages = models.CharField(max_length=255)
    HowManyBirths=models.IntegerField()
    Miscarriageage = models.CharField(max_length=255)
    Miscarriage_year = models.CharField(max_length=255)

    def __str__(self):
        return self.Mothers_name


class Visit(models.Model):
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
