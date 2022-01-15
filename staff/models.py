from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from account.models import *

# Create your models here.

class Ebook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    book_name=models.CharField(max_length=200)
    author=models.CharField(max_length=50)
    book_file=models.FileField(upload_to='book_file',blank=True,null=True)
    link=models.URLField(blank=True,null=True)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    def __str__(self):
        return str(self.book_name)

class StudentBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True,null=True)
    year_of_admission=models.PositiveIntegerField(validators=[MinValueValidator(1900),MaxValueValidator(3000)])
    book_name=models.CharField(max_length=50)
    edition=models.CharField(max_length=100,blank=True,null=True)
    author=models.CharField(max_length=100)
    issue_date=models.DateField()
    due_date=models.DateField()
    return_date=models.DateField()
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.book_name)


