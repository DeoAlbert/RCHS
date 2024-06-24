from rest_framework import serializers
from .models import HealthcareWorker
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth import authenticate

#password = serializers.CharField(max_length=68, min_length=6, write_only=True)

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthcareWorker
        fields = ("user_id","username","email","first_name","middle_name","last_name","occupation","password")
        extra_kwargs = {'password': {'write_only': True}}
        #extra_kwargs = {'is_active': {'default': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance     
        
# min_length=6
# min_length=3
#username = serializers.CharField(max_length=255)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,write_only=True)
    email = serializers.EmailField()
    tokens = serializers.SerializerMethodField()
    def get_tokens(self, obj):
        user = HealthcareWorker.objects.get(email=obj['email'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
    class Meta:
        model = HealthcareWorker
        fields = ['email','password','tokens']
    def validate(self, validated_data):
        email = validated_data.pop('email', None)
        password = validated_data.pop('password', None)

        user = auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }



# class LoginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=68, write_only=True)
#     username = serializers.CharField(max_length=255)
#     tokens = serializers.SerializerMethodField()

#     def get_tokens(self, obj):
#         user = HealthcareWorker.objects.get(username=obj['username'])
#         return {
#             'refresh': user.tokens()['refresh'],
#             'access': user.tokens()['access']
#         }

#     class Meta:
#         model = HealthcareWorker
#         fields = ['password', 'username', 'tokens']

#     def validate(self, validated_data):
#         username = validated_data.pop('username', None)
#         password = validated_data.pop('password', None)

#         user = authenticate(username=username, password=password)
#         if not user:
#             raise AuthenticationFailed('Invalid credentials, try again')
#         if not user.is_active:
#             raise AuthenticationFailed('Account disabled, contact admin')
#         return {
#             'email': user.email,
#             'username': user.username,
#             'tokens': self.get_tokens(validated_data)
#         }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')