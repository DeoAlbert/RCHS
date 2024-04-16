
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

 # created a custom manager model
class CustomAccountManager(BaseUserManager):
    def create_user(self,email,user_name, first_name,last_name,password,**other_fields):

        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        user = self.model(email =email,user_name= user_name, first_name = first_name,last_name = last_name,**other_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email,user_name, first_name,last_name,password,**other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Super user must be assigned to is_staff = True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Super user must be assigned to is_superuser = True")
        if not email:
            raise ValueError("You must provide an email address")

        # email = self.normalize_email(email)
        # user = self.model(email =email,user_name= user_name, first_name = first_name,last_name = last_name,**other_fields)
        # user.set_password(password)
        # user.save()
        # return user

        return self.create_user(email,user_name, first_name,last_name,password,**other_fields)





# created a custom user model
class HealthcareWorker(AbstractBaseUser,PermissionsMixin):
    user_id = models.CharField(max_length=255,unique=True)
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    start_date= models.DateTimeField(default=timezone.now)
    is_staff= models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email","user_id", "first_name","last_name"]

    def __str__(self):
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

