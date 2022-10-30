from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError("you must create an email")
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(email, **other_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Parent(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=256)


class Student(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    age = models.IntegerField()

    parent = models.ForeignKey(Parent, on_delete=models.PROTECT)
    subject = models.ManyToManyField(Subject)

    class Meta:
        constraints = [
            models.CheckConstraint(name="first_name_only_letters", check=~models.Q(
                first_name__contains="[^a-zA-Z]"))
        ]
