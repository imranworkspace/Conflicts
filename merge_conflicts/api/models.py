from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    # added by v1
    mobile=models.IntegerField()







































































