from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
     def create_user(self, username,password,email=None,full_name=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("Users must have an Username")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            email = self.username

        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj



class User(AbstractBaseUser):
    username = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = []
    objects=UserManager()
