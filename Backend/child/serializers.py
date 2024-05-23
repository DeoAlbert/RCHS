from rest_framework import serializers
from mother.models import Mother
from .models import Child_visit, Child, Consultation_Visit_Child

# void
# class ChildSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= Child
#         fields= "__all__"


class ChildSerializer(serializers.HyperlinkedModelSerializer):
    mother_name = serializers.CharField(write_only=True)
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
        
        child = Child.objects.create(mother=mother, **validated_data)
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
    class Meta:
        model = Child
        fields = ['child_name', 'child_gender', 'mother']

class ChildVisitSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_visit
        fields = ['visit_number', 'date']



