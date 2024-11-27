from django.db import models

# Create your models here.
class project_user(models.Model):
    Name=models.TextField()
    Age=models.IntegerField()
    Email=models.EmailField()
    Place=models.TextField()
