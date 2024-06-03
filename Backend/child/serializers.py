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
        fields = ['url', 'id', 'child_name', 'healthcare_centre_name', 'mother_name', 'mother', 'child_number', 'child_gender', 'date_of_birth', 'weight_at_birth', 'length_at_birth', 'place_of_birth', 'maternal_health_worker', 'child_residence']
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


class ChildVisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Child_visit
        fields= "__all__"

class ChildConsultationVisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Consultation_Visit_Child
        fields= "__all__"

class ChildSummarySerializer(serializers.ModelSerializer):

    age = serializers.SerializerMethodField()
    class Meta:
        model = Child
        fields = ['child_name', 'child_gender', 'mother_name', 'age']
    
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

class ChildVisitSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_visit
        fields = ['weight_grams','height','date']



