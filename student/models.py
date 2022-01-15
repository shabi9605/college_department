from re import M, U
from django.db import models
from django.contrib.auth.models import User
from django.db.models.lookups import Transform
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from datetime import MAXYEAR, MINYEAR, datetime
from django.core.validators import BaseValidator, MaxLengthValidator, MaxValueValidator, MinValueValidator
from account.models import *
import datetime

# Create your models here.

management='management'
community='community'
types=[(management,'management'),(community,'community')]

appering='appering'
passout='passout'

status=[(appering,'appering'),(passout,'passout')]




def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Basic_Details(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    adhar_no=models.PositiveIntegerField()
    dob=models.DateField()
    house_name=models.CharField(max_length=50)
    place=models.CharField(max_length=100,)
    pincode=models.PositiveIntegerField(validators=[MinValueValidator(100000), MaxValueValidator(1000000)])
    mobile_no=PhoneNumberField()
    application_id=models.IntegerField(blank=True,null=True)


    def __str__(self):
        return str(self.name)

class Application(models.Model):
    name=models.ForeignKey(Basic_Details,on_delete=models.CASCADE,blank=True,null=True)
    application_id=models.IntegerField(blank=True,null=True)
    landmark=models.CharField(max_length=50,)
    district=models.CharField(max_length=40,choices=District_name,default=Thrissur)
    mobile_no2=PhoneNumberField(blank=True,null=True)
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    religion=models.CharField(max_length=30)
    cast=models.CharField(max_length=40)

    photo=models.ImageField(upload_to='register_image')
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    course_name_previous_college=models.CharField(max_length=50)
    management_or_community_status=models.CharField(max_length=30,choices=types,)
    appering_or_passout=models.CharField(max_length=20,choices=status,default=passout)
    persentage_obtained=models.CharField(max_length=50,blank=True,null=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

class PreacdemicDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    sslc_school_name=models.CharField(max_length=100)
    sslc_Persentage=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(101)])
    sslc_passout_year=models.IntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    higher_secondary_school_name=models.CharField(max_length=100)
    hss_persentage=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(101)])
    hss_passout_year=models.IntegerField()
    college_name=models.CharField(max_length=100,blank=True,null=True)
    course_name=models.CharField(max_length=100,blank=True,null=True)
    college_passout_year=models.IntegerField()
    year_gap=models.PositiveIntegerField(blank=True,null=True)
    institution_last_studied=models.CharField(max_length=100)
    approve=models.BooleanField(default=False)

    def __str__(self):
        return str(self.student)


class Complaint(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    complaint=models.TextField()
    replay=models.TextField(blank=True,null=True,default='not replayed')
    created_date=models.DateField(auto_now_add=True)
    replay_date=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.student)


class ChalanGeneration(models.Model):
    chalan_no=models.IntegerField(blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    purpose_of_this_chalan=models.CharField(max_length=200)
    student_name=models.CharField(max_length=100)
    register_no=models.IntegerField()
    address=models.TextField()
    dob=models.DateField()
    mobile_no=PhoneNumberField()    
    email=models.EmailField()
    amount=models.PositiveIntegerField()
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.student_name)



 

