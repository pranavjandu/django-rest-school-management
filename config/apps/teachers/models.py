from django.db import models
from apps.users.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from config.settings import IMAGE_UPLOAD_PATH

class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    MARITAL_CHOICES = (
        ('SINGLE', "Single"),
        ('MARRIED', "Married"),
        ('DIVORCED', "Divorced"),
        ('SEPARATED', "Separated"),
        ('WIDOWED', "Widowed"),)  
    
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    personnel_number = models.PositiveIntegerField()
    first_name=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    dob = models.DateField(null=True, blank=True)
    birthplace = models.CharField(max_length=255,null=True,blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=9, choices=MARITAL_CHOICES,null=True,blank=True)
    contact_number = PhoneNumberField(null=True, blank=True, unique=True)
    alternate_number = PhoneNumberField(null=True, blank=True, unique=True)
    nationality = CountryField(null=True, blank=True)
    photo = models.ImageField(upload_to =IMAGE_UPLOAD_PATH, null=True, blank=True) 
    emergency_contact_name = models.CharField(max_length=255,null=True,blank=True)
    emergency_contact_number = PhoneNumberField(null=True, blank=True, unique=True)
    address_line1 = models.CharField(max_length=255,null=True,blank=True)
    address_line2 = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    zipcode = models.CharField(max_length=255,null=True,blank=True)
    country = CountryField(null=True, blank=True)
    objects = models.Manager()

    def __str__(self): 
        return (self.first_name+" "+self.last_name)

