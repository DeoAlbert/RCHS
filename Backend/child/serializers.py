from rest_framework import serializers
from .models import Child_visit, Child, Consultation_Visit_Child

class ChildSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Child
        fields= "__all__"


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
