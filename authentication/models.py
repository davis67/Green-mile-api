from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta

class UserManager(BaseUserManager):
    def create_user(self, username, name, email, phone_number, role, password=None):

        if username is None:
            raise TypeError("Users should have a username")

        if name is None:
            raise TypeError("Name field is required")

        if email is None:
            raise TypeError("EmailField is required")

        user = self.model(username=username, email=self.normalize_email(email))

        user.set_password(password);

        user.save()

        return user

    def create_superuser(self, email, name, username,role, phone_number, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user  = self.create_user(username, name, email,role, phone_number, password)

        user.is_superuser = True

        user.is_staff = True

        user.is_verified = True

        user.save()

        return user


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=255,  db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    role = models.CharField(max_length=255, db_index=True)
    phone_number = models.CharField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username", "name", "role", "phoneNumber"]

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        access = refresh.access_token
        access.set_exp(lifetime = timedelta(days = 10))
        return {
        "refresh": str(refresh),
        "access": str(access),
        }
