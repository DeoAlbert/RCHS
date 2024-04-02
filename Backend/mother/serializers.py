from rest_framework import serializers
from .models import Mother, Visit

class MotherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Mother
        fields= "__all__"


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Visit
        fields= "__all__"