from django.db import models

# Create your models here.
from datetime import datetime
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import BaseValidator
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - \
           ((today.month, today.day) < (born.month, born.day))

@deconstructible
class MinAgeValidator(BaseValidator):
    message = _("Age must be at least %(limit_value)d.")
    code = 'min_age'

    def compare(self, a, b):
        return calculate_age(a) < b

OPTED =[
    ('5',5),
    ('6',6),
    ('7',7),
    ('8',8),
    ('9',9),
    ('10',10),
]
from rest_framework import serializers
class Student(models.Model):
    stu_name =models.CharField(max_length=100)
    stu_father =models.CharField(max_length=100)
    dob =models.DateField(validators=[MinAgeValidator(10)])
    address = models.TextField()
    city = models.CharField(max_length=50)
    state =models.CharField(max_length=50)
    pin = models.CharField(max_length=6)
    phone =models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    class_opted =models.CharField(max_length=20, choices=OPTED)
    date = models.DateTimeField(auto_now=True)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.stu_name

    class Meta:
        db_table ='students'


