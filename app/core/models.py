from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings

#1.2 Created cutom usermodel and Usermanager based on Base classes
class UserManager(BaseUserManager):

    #1.3 Did that to reassign create_user func to receive email instead of uname
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves new user"""
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=email.lower(), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password):
        """Creates a superuser"""
        superuser = self.create_user(
            email,
            password,
            is_superuser=True,
            is_staff=True
        )

        superuser.save(using=self._db)
        return superuser


#1.4 Created a custom User model with email instead of username
class User(AbstractBaseUser, PermissionsMixin):

    """Custom usermodel that supports using email rather than username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #1.5 Added my custom usermanager
    objects = UserManager()
    #1.6 Replaced default field from username to email
    #   next, go to settings.py
    USERNAME_FIELD = 'email'


class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, #if you delete the user, tags're also deleted
    )

    def __str__(self):
        return self.name
