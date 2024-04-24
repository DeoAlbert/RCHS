from rest_framework import serializers
from .models import Mother, Mother_visit

class MotherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Mother
        fields= "__all__"


class MotherVisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Mother_visit
        fields= "__all__"