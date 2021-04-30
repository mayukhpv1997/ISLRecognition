from django.db import models

# Create your models here.
class Signup(models.Model):
    firstname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirmpassword = models.CharField(max_length=30)





