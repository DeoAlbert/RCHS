from django.db import models

# Create your models here.

class Mother (models.Model):
    jina_la_kliniki= models.CharField(max_length=255)
    jina_la_mama=models.CharField(max_length=255)
    namba_ya_uandikishaji=models.IntegerField()
    namba_ya_hati_punguzo_ya_chandarua=models.IntegerField()
    umri=models.IntegerField()
    elimu=models.CharField(max_length=255)
    kazi=models.CharField(max_length=255)
    jina_la_mume_mwenzi=models.CharField(max_length=255)
    mume_mwenzi_umri=models.IntegerField()
    mume_mwenzi_elimu=models.CharField(max_length=255)
    mume_mwenzi_kazi=models.CharField(max_length=255)
    kjjimtaa_kitongoji=models.CharField(max_length=255)
    jina_la_mwenyekiti=models.CharField(max_length=255)
    mimba_ya_ngapi=models.IntegerField()
    watoto_walio_hai=models.IntegerField()
    amezaa_marangapi_ngapi=models.IntegerField()

    def __str__(self):
        return self.jina_la_mama


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
