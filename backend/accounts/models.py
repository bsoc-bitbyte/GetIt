from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True

        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    phone_regex = RegexValidator(regex=r'^(\+91)?\d{10}$', message="Invalid phone number")

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13, validators=[phone_regex], blank=True)
    address = models.CharField(max_length=128,  blank=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
