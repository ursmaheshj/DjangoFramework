from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError("User must have a valid email")
        user = self.model(email=self.normalize_email(email)) 
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be a staff")

        user = self.create_user(email,password)
        user.is_staff = True
        user.is_seller = True
        user.is_customer = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=50,unique=True,blank=False,null=False)
    city = models.CharField(max_length=50)
    password = models.CharField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self,obj=None):
        return self.is_superuser

    def has_module_perms(self,app_label):
        return self.is_superuser