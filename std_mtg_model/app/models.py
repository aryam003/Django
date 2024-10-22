from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.IntegerField()
    name=models.TextField()
    email=models.EmailField()
    ph_no=models.IntegerField()