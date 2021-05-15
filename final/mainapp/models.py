from django.db import models

# Create your models here.



class sender(models.Model):
    name = models.CharField(max_length=100)
    cell = models.CharField(max_length=100 )
    Email =  models.CharField(max_length=100 )
    message =  models.CharField(max_length=1000)
    def __str__(self):
        return self.Email



class user(models.Model):
    firstName = models.CharField(max_length=100 )
    lastName = models.CharField(max_length=100 )
    cell = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    email =  models.CharField(max_length=100 )
    password =  models.CharField(max_length=100 )
    plan =  models.CharField(max_length=100 )
    def __str__(self):
        return self.email

    

