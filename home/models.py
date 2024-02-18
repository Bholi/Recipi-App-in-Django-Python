from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    email = models.EmailField(null = True, blank = True)
    address = models.CharField(max_length = 50,null = True, blank = True)
   

