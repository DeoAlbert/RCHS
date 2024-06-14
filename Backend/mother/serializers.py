from rest_framework import serializers
from .models import Mother, Mother_visit
from datetime import date


class MotherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mother
        fields = [
            'url',
            'id',
            'healthcare_centre_name',
            'mother_name',
            'registration_number',
            'mosquito_net_voucher_number',
            'mother_age',
            'mother_education',
            'mother_employment',
            'height',
            'partner_name',
            'partner_age',
            'partner_work',
            'partner_education',
            'residential_region',
            'residential_district',
            'Chairperson_name',
            'pregnancies',
            'alive_children',
            'miscarriages',
            'births',
            'registrant_type',
            'parent_type',
            'gender'
        ]



class MotherVisitSerializer(serializers.HyperlinkedModelSerializer):
    mother_name = serializers.CharField()
    mother = serializers.HyperlinkedRelatedField(view_name='mother-detail', read_only = True)

    class Meta:
        model = Mother_visit
        fields = [
            'url',
            'id',  # Primary key, automatically added by Django
            'mother',
            'mother_name',
            'visit_number',
            'visit_date',
            'body_temperature',
            'blood_pressure',
            'hb_percentage',
            'pmtct_nutrition',
            'breastfeeding',
            'milk_coming_out',
            'breastfeeding_within_hour',
            'sore_nipples',
            'full_nipples',
            'abscesses',
            'breastfeeding_advice',
            'uterus_shrinking',
            'uterus_pain',
            'incision_did_not_tear',
            'incision_type',
            'wound_healed',
            'pus',
            'wound_open',
            'bad_smell',
            'lochia_amount',
            'lochia_color',
            'mental_state',
            'mental_issues',
            'advice_given',
            'ferrous_sulphate',
            'folic_acid',
            'tetanus_toxoid_doses',
            'pmtct_ctx',
            'postpartum_medications',
            'vitamin_a',
            'date_of_next_visit',
            'provider_name',
            'provider_title',]
    
        extra_kwargs = {
            'mother': {'read_only': True}
        }

    def create(self, validated_data):
        mother_name = validated_data.pop('mother_name')
        try:
            mother = Mother.objects.get(mother_name=mother_name)
        except Mother.DoesNotExist:
            raise serializers.ValidationError(f"Mother with name {mother_name} does not exist.")
        
        mother_visit = Mother_visit.objects.create(mother=mother, mother_name = mother_name,**validated_data)
        return mother_visit



class MotherSummarySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Mother
        fields = ['url','id', 'mother_name', 'mother_age', 'partner_name']
    

class MotherVisitSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mother_visit
        fields = ['id','visit_number', 'visit_date']