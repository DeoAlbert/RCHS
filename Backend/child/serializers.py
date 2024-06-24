from rest_framework import serializers
from mother.models import Mother
from .models import Child_visit, Child, Consultation_Visit_Child
from datetime import date

# void
# class ChildSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= Child
#         fields= "__all__"

class ChildSerializer(serializers.HyperlinkedModelSerializer):
    mother_name = serializers.CharField()
    mother = serializers.HyperlinkedRelatedField(view_name='mother-detail', read_only = True)

    class Meta:
        model = Child
        fields = ['url', 'id', 'child_name', 'healthcare_centre_name', 'mother_name', 'mother', 'child_number', 'child_gender', 'date_of_birth', 'weight_at_birth', 'length_at_birth', 'birth_region', 'birth_district', 'residential_region','residential_district','maternal_health_worker']
        extra_kwargs = {
            'mother': {'read_only': True}
        }

    def create(self, validated_data):
        mother_name = validated_data.pop('mother_name')
        try:
            mother = Mother.objects.get(mother_name=mother_name)
        except Mother.DoesNotExist:
            raise serializers.ValidationError(f"Mother with name {mother_name} does not exist.")
        
        child = Child.objects.create(mother=mother, mother_name = mother_name,**validated_data)
        return child


# class ChildVisitSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= Child_visit
#         fields= "__all__"

class ChildVisitSerializer(serializers.HyperlinkedModelSerializer):
    child_name = serializers.CharField()
    child = serializers.HyperlinkedRelatedField(view_name='child-detail', read_only = True)

    class Meta:
        model = Child_visit
        fields = [
            'url',
            'id',  # Primary key, automatically added by Django
            'child',
            'child_name',
            'visit_number',
            'date',
            'child_growth_and_development_status',
            'return_date',
            'bcg_tuberculosis_injection_right_shoulder',
            'polio',
            'dpt_hep_b',
            'pneumococcal',
            'rota',
            'measles',
            'vitamin_a',
            'deworming_medication',
            'weight_grams',
            'height',
            'anemia',
            'body_temperature',
            'exclusive_breastfeeding',
            'replacement_milk',
            'unable_to_breastfeed',
            'child_play',
            'eyes',
            'mouth',
            'ears',
            'navel_healed',
            'navel_red',
            'navel_discharge_odor',
            'has_pus_filled_bumps',
            'has_turned_yellow',
            'received_bcg',
            'received_polio_0',
            'received_polio_1',
            'received_dtp_hep_hib',
            'received_pneumococcal',
            'received_rota',
            'name_of_attendant',
            'attendant_title',
            'other_issues',]
    
        extra_kwargs = {
            'child': {'read_only': True}
        }

    def create(self, validated_data):
        child_name = validated_data.pop('child_name')
        try:
            child = Child.objects.get(child_name=child_name)
        except Child.DoesNotExist:
            raise serializers.ValidationError(f"Child with name {child_name} does not exist.")
        
        child_visit = Child_visit.objects.create(child=child, child_name = child_name,**validated_data)
        return child_visit


# class ChildConsultationVisitSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= Consultation_Visit_Child
#         fields= "__all__"

class ChildConsultationVisitSerializer(serializers.HyperlinkedModelSerializer):
    child_name = serializers.CharField()
    child = serializers.HyperlinkedRelatedField(view_name='child-detail', read_only = True)

    class Meta:
        model = Consultation_Visit_Child
        fields = [
            'url',
            'id', 
            'child',
            'child_name',
            'date',
            'visit_type',
            'weight', 
            'height',    
            'temperature',    
            'other',
            'test_results', 
            'additional_notes'
            ]
    
        extra_kwargs = {
            'child': {'read_only': True}
        }

    def create(self, validated_data):
        child_name = validated_data.pop('child_name')
        try:
            child = Child.objects.get(child_name=child_name)
        except Child.DoesNotExist:
            raise serializers.ValidationError(f"Child with name {child_name} does not exist.")
        
        consultation_Visit_Child = Consultation_Visit_Child.objects.create(child=child, child_name = child_name,**validated_data)
        return consultation_Visit_Child

class ChildSummarySerializer(serializers.HyperlinkedModelSerializer):

    age = serializers.SerializerMethodField()
    class Meta:
        model = Child
        fields = ['url','id','child_name', 'child_gender', 'mother_name', 'age']
    
    def get_age(self, obj):
        today = date.today()
        # Calculate the difference in years
        year_difference = today.year - obj.date_of_birth.year
        # Calculate the difference in months
        month_difference = today.month - obj.date_of_birth.month
        # Calculate the difference in days
        day_difference = today.day - obj.date_of_birth.day
        
        # Adjust year and month differences if needed
        if day_difference < 0:
            month_difference -= 1
        if month_difference < 0:
            year_difference -= 1
            month_difference += 12
        
        return f"{year_difference} years, {month_difference} months"

class ChildVisitSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Child_visit
        fields = ['id','weight_grams','height','date','visit_number']



