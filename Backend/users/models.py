from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


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
    user_name = models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    start_date= models.DateTimeField(default=timezone.now)
    is_staff= models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["email","user_name", "first_name","last_name"]

    def __str__(self):
        return self.user_name

