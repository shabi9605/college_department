from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields.related import ForeignKey
from django.db.models.lookups import EndsWith
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
import datetime

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

Thiruvananthapuram = 'Thiruvananthapuram'
Kollam = 'Kollam'
Alappuzha= 'Alappuzha'
Pathanamthitta = 'Pathanamthitta'
Kottayam = 'Kottayam'
Idukki = 'Idukki'
Ernakulam = ' Ernakulam'
Thrissur= 'Thrissur'
Palakkad = 'Palakkad'
Malappuram = 'Malappuram'
Kozhikode = ' Kozhikode'
Wayanadu= 'Wayanadu'
Kannur = 'Kannur'
Kasaragod = 'Kasaragod'

District_name =(
    (Thiruvananthapuram , 'Thiruvananthapuram'),
    (Kollam , 'Kollam'),
    (Alappuzha , 'Alappuzha'),
    (Pathanamthitta , 'Pathanamthitta'),
    (Kottayam , 'Kottayam'),
    (Idukki , 'Idukki'),
    ( Ernakulam , ' Ernakulam'),
    (Thrissur, 'Thrissur'),
    (Palakkad , 'Palakkad'),
    (Malappuram , 'Malappuram'),
    (Kozhikode, ' Kozhikode'),
    (Wayanadu, 'Wayanadu'),
    (Kannur , 'Kannur'),
    (Kasaragod , 'Kasaragod')
)

Male = 'Male'
Female = 'Female'
GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
]

teacher='teacher'
HOD='HOD'
job_types=[(teacher,'teacher'),(HOD,'HOD')]

office_staff='office staff'
librarian='librarian'
lab_assistant='lab assistant'
other='other'
non_job_type=[(office_staff,'office staff'),(librarian,'librarian'),
(lab_assistant,'lab assistant'),(other,'other')]




class Course(models.Model):
    course_name=models.CharField(max_length=50)
    description=models.CharField(max_length=20)
    course_prefix=models.CharField(max_length=20)
    duration=models.CharField(max_length=50)
    no_of_semsters=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    admission_fee=models.PositiveIntegerField()
    tution_fee=models.PositiveIntegerField()
    library_fee=models.PositiveIntegerField()

    def __str__(self):
        return str(self.course_name)


    
class Semester(models.Model):
    title=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.title)

class Subject(models.Model):
    title=models.CharField(max_length=50)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    semster=models.ForeignKey(Semester,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

class Syllabus(models.Model):
    name=models.CharField(max_length=50)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    link=models.URLField(blank=True,null=True)
    syllabus=models.FileField(upload_to='syllabus')
    def __str__(self):
        return str(self.name)

class Notification(models.Model):
    title=models.CharField(max_length=50)
    notification=models.CharField(max_length=200)
    notification_publish_date=models.DateTimeField(default=timezone.now)
    starting_date=models.DateTimeField(default=timezone.now)
    ending_date=models.DateTimeField(default=timezone.now)
    notification_type=models.CharField(max_length=100,blank=True,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    semster=models.ForeignKey(Semester,on_delete=models.CASCADE)
    link=models.URLField(blank=True,null=True)
    file=models.FileField(upload_to='notification',blank=True,null=True)
    approve=models.BooleanField(default=False)
    def __str__(self):
        return str(self.title)


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField()
    admission_no=models.CharField(max_length=30)
    register_no=models.CharField(unique=True,max_length=30)
    application_id=models.CharField(max_length=30,blank=True,null=True)
    
    name=models.CharField(max_length=40)
    adhar_no=models.PositiveIntegerField()
    dob=models.DateField()
    house_name=models.CharField(max_length=50)
    place=models.CharField(max_length=100,)
    landmark=models.CharField(max_length=50,)
    district=models.CharField(max_length=40,choices=District_name,default=Thrissur)

    pincode=models.PositiveIntegerField(validators=[MinValueValidator(100000), MaxValueValidator(1000000)])
    mobile_no=PhoneNumberField(unique=True)
    mobile_no2=PhoneNumberField(blank=True,null=True)
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    religion=models.CharField(max_length=30)
    cast=models.CharField(max_length=40)

    semster=models.ForeignKey(Semester,on_delete=models.CASCADE)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    date_of_admission=models.DateField()

    parent_name=models.CharField(max_length=50)
    local_guardian=models.CharField(max_length=50,blank=True,null=True)
    photo=models.ImageField(upload_to='register_image',default='default.jpg')
    

    def __str__(self):
        return str(self.user)

class Parent(models.Model):
    admission_no=models.OneToOneField(Student,on_delete=models.CASCADE,blank=True,null=True)
    parent=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    mothers_mobile_no=PhoneNumberField(blank=True,null=True)
    fathers_mobile_no=PhoneNumberField()
    email=models.EmailField()



class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    email=models.EmailField()

    teacher_id=models.IntegerField(unique=True)
    dob=models.DateField()
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    
    mobile_no=PhoneNumberField(unique=True)
    mobile_no2=PhoneNumberField(blank=True,null=True)
    
    house_name=models.CharField(max_length=50,blank=True,null=True)
    place=models.CharField(max_length=100,blank=True,null=True)
    pincode=models.PositiveIntegerField(blank=True,null=True)
    district=models.CharField(max_length=40,choices=District_name,default=Thrissur)
    
    designation=models.CharField(max_length=60,)
    
    job_type=models.CharField(max_length=50,choices=job_types,default=teacher)
    
    department_post=models.CharField(max_length=100)
    qualification=models.CharField(max_length=40)
    other_qualifications=models.CharField(max_length=100,blank=True,null=True)
    certificate_proof=models.FileField(upload_to='certificate_teacher')
    mphill=models.BooleanField(default=False)
    phd=models.BooleanField(default=False)
    net=models.BooleanField(default=False)
    year_of_experience=models.CharField(max_length=30)

    photo=models.ImageField(upload_to='teacher_image')
    confirmed='confirmed'
    not_confirmed='not_confirmed'
    confirmations=[
        (confirmed,'confirmed'),
        (not_confirmed,'not_confirmed')
    ]
    confirmation=models.CharField(max_length=20,choices=confirmations,default=not_confirmed)

    def __str__(self):
        return str(self.user)


class NonTeaching_Staff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    email=models.EmailField()
    dob=models.DateField()
    staff_id=models.IntegerField(unique=True)
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    
    mobile_no=PhoneNumberField(unique=True)
    mobile_no2=PhoneNumberField(blank=True,null=True)

    house_name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pincode=models.PositiveIntegerField()
    photo=models.ImageField(upload_to='non_teaching_photo')
    district=models.CharField(max_length=40,choices=District_name,default=Thrissur)
    
    job_type=models.CharField(max_length=50,choices=non_job_type,default=librarian)
    post=models.CharField(max_length=100)
    qualification=models.CharField(max_length=40)
    other_qualifications=models.CharField(max_length=100,blank=True,null=True)
    certificate_proof=models.FileField(upload_to='certificate_teacher')
    
    degree=models.BooleanField(default=False)
    plus_two=models.BooleanField(default=False)
    sslc=models.BooleanField(default=False)
    year_of_experience=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='staff_image')

    def __str__(self):
        return str(self.user)



# class Contact(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.EmailField()
#     subject=models.CharField(max_length=300)
#     message=models.TextField()

#     def __str__(self):
#         return str(self.name)