from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16)
    email = models.EmailField()

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
            models.CheckConstraint(name="first_name_only_letters", check=~models.Q(first_name__contains="[^a-zA-Z]"))
        ]