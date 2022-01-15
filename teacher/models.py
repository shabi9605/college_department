from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from account.models import *
# Create your models here.
monday='monday'
tuesday='tuesday'
wednesday='wednesday'
thursday='thursday'
friday='friday'
saturday='saturday'

days=[(monday,'monday'),
(tuesday,'tuesday'),
(wednesday,'wednesday'),
(thursday,'thursday'),
(saturday,'saturday')]

class TimeTable(models.Model):
    title=models.CharField(max_length=50)
    day=models.CharField(max_length=50,choices=days,default=monday)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    semster=models.ForeignKey(Semester,on_delete=models.CASCADE)
    subject1=models.CharField(max_length=50)
    subject2=models.CharField(max_length=50)
    subject3=models.CharField(max_length=50)
    subject4=models.CharField(max_length=50)
    subject5=models.CharField(max_length=50)
    subject6=models.CharField(max_length=50,blank=True,null=True)
    appruve=models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)

class Audio_Video(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=50)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,blank=True,null=True)
    description=models.CharField(max_length=100,blank=True,null=True)
    audio=models.FileField(upload_to='audio',blank=True,null=True)
    video=models.FileField(upload_to='video',blank=True,null=True)
    link=models.URLField(blank=True,null=True)
    created_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)

class Assignment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    semster=models.ForeignKey(Semester,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    question=models.FileField(upload_to='assignment_question',blank=True,null=True)
    answer=models.FileField(upload_to='assignment_answer',blank=True,null=True)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.title)

class InternalMark(models.Model):
    user=models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    semster=models.ForeignKey(Semester,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    test1_mark=models.PositiveIntegerField()
    test2_mark=models.PositiveIntegerField()
    seminar_mark=models.PositiveIntegerField()
    attendence=models.PositiveIntegerField()
    no_of_working_days=models.PositiveIntegerField()
    attendence_mark=models.PositiveIntegerField()
    total_seminar_mark=models.PositiveIntegerField()
    total_internal_mark=models.PositiveIntegerField()
    final_total_internal_mark=models.PositiveIntegerField()

    def __str__(self):
        return str(self.student)
