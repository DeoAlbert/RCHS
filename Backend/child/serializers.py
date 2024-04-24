from rest_framework import serializers
from .models import Child_visit, Child

class ChildSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Child
        fields= "__all__"


class ChildVisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Child_visit
        fields= "__all__"