from django.db import models


class StudentProfileModel(models.Model):
    name=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=100)
    note=models.CharField(max_length=500)
