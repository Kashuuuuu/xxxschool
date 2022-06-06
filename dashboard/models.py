from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class frgt_pwd(models.Model):
   
    frg_token=models.CharField(max_length=1000)
    def __str__(self):
        return self.user.username

class admin_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='admin_record')
    img=models.ImageField(null=True)
    name=models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.IntegerField(null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    address=models.TextField(blank=True,null=True)
    def __str__(self) -> str:
        return self.name        


class professor(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    joining_date = models.DateField()
    password = models.CharField(max_length=1000)
    confirm_password = models.CharField(max_length=1000)
    mobile = models.IntegerField()
    gender = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    dob = models.DateField()
    education = models.CharField(max_length=100)
    image = models.ImageField()

class student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    education = models.CharField(max_length=100,null=True)
    registration_date = models.DateField()
    roll_no = models.CharField(max_length=1000)
    sub_class = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mobile = models.IntegerField()
    parent_name = models.CharField(max_length=100)
    parent_mobile = models.IntegerField()
    dob = models.DateField()
    blood_group = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    image = models.ImageField()    
