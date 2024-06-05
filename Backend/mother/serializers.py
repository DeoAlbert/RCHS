from rest_framework import serializers
from .models import Mother, Mother_visit

# class MotherSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= Mother
#         fields= "__all__"

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
            'Height',
            'partner_name',
            'partner_age',
            'partner_work',
            'partner_education',
            'address',
            'Chairperson_name',
            'pregnancies',
            'alive_children',
            'miscarriages',
            'births',
            'miscarriage_age',
            'miscarriage_year',
        ]


class MotherVisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Mother_visit
        fields= "__all__"


class MotherSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        fields = ['mother_name', 'mother_age']

class MotherVisitSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother_visit
        fields = ['visit_number', 'visit_date']