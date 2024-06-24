from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self,email,username, first_name,middle_name,last_name,occupation,password,**extra_fields):
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', True)
        user = self.model(email = email,username=username,first_name=first_name,middle_name=middle_name,last_name=last_name,occupation=occupation, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    
    
    def create_superuser(self,email,username, first_name,middle_name,last_name,occupation,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super user must be assigned to is_staff = True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super user must be assigned to is_superuser = True")
        if not email:
            raise ValueError("You must provide an email address")
        
        return self._create_user(email=email,username=username, first_name=first_name,middle_name=middle_name,last_name=last_name,occupation=occupation,password=password,**extra_fields)
    

# created a custom user model
class HealthcareWorker(AbstractUser,PermissionsMixin):
    user_id = models.CharField(max_length=255,unique=True)
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    first_name= models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    start_date= models.DateTimeField(default=timezone.now)
    is_staff= models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","user_id", "first_name","middle_name","last_name","occupation",]

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

    
    

