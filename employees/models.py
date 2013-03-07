import datetime

from django.db import models
from django.utils import timezone

class Employee(models.Model):
    name = models.CharField(max_length=200)
    employee_id = models.AutoField(primary_key=True) 

    def __unicode__(self):
        return self.name

class BioData(models.Model):
    employee = models.OneToOneField(Employee)
    age = models.IntegerField()
    sex = models.CharField(max_length=20)

    def __unicode__(self):
        return self.employee.name

class Payroll(models.Model):
    employee = models.OneToOneField(Employee)
    salary = models.FloatField()

    def __unicode__(self):
        return self.employee.name
