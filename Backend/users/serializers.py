from rest_framework import serializers
from .models import HealthcareWorker


class RegisterHealthcareWorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthcareWorker
        fields = ("user_id","user_name","email","first_name","last_name")
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance