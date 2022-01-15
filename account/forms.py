from django import forms
from django.forms.widgets import PasswordInput, Widget
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import NumberInput


# class UserForm(forms.ModelForm):
    
#     class Meta:
#         model=User
#         fields=('email',)

class UserForm1(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text='Please enter teacher id with teacher(eg:1234teacher)',widget=PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','email','password1','password2',)

class UserForm2(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text='Please enter staff id with staff(eg:123staff,)',widget=PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','email','password1','password2',)

class UpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('email',)
        
class StudentForm(forms.ModelForm):
    dob=forms.DateField(required=True, widget=NumberInput(attrs={'type':'date'}))
    date_of_admission=forms.DateField(required=True, widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model=Student
        fields=('application_id','register_no','name','email','adhar_no',
        'dob','house_name','place','landmark','district','pincode','mobile_no','mobile_no2',
        'gender','religion','cast','semster','course_name','date_of_admission',
        'parent_name','local_guardian','photo')

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('house_name','place','landmark','district','pincode','photo','mobile_no2')

class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('register_no','application_id','name','adhar_no',
        'dob','house_name','place','landmark','district','pincode','mobile_no','mobile_no2',
        'gender','religion','cast','semster','course_name','date_of_admission',
        'parent_name','local_guardian','photo')

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('name','email','dob','house_name','place','district','pincode','mobile_no','mobile_no2',
        'gender','designation','job_type','department_post','qualification','other_qualifications',
        'certificate_proof','mphill','phd','net','year_of_experience','photo')

class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('name','dob','house_name','place','district','pincode','mobile_no','mobile_no2',
        'gender','designation','job_type','department_post','qualification','other_qualifications',
        'certificate_proof','mphill','phd','net','year_of_experience','photo')


class HodUpdateTeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('name','dob','house_name','place','district','pincode','mobile_no','mobile_no2',
        'gender','designation','job_type','department_post','qualification','other_qualifications',
        'certificate_proof','mphill','phd','net','year_of_experience','photo','confirmation')

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('house_name','place','district','pincode','photo','mobile_no','mobile_no2')


class NonTeachingStaffForm(forms.ModelForm):
    class Meta:
        model=NonTeaching_Staff
        fields=('name','email','dob','house_name','place','district','pincode','mobile_no','mobile_no2',
        'gender','job_type','post','qualification','other_qualifications',
        'certificate_proof','degree','plus_two','sslc','year_of_experience','photo')


class UpdateNonTeachingStaffForm(forms.ModelForm):
    class Meta:
        model=NonTeaching_Staff
        fields=('name','dob','house_name','place','district','pincode','mobile_no','mobile_no2',
        'gender','job_type','post','qualification','other_qualifications',
        'certificate_proof','degree','plus_two','sslc','year_of_experience','photo')


class NonTeachingStaffPrfileForm(forms.ModelForm):
    class Meta:
        model=NonTeaching_Staff
        fields=('house_name','place','district','pincode','photo','mobile_no','mobile_no2')




class ParentForm(forms.ModelForm):
    class Meta:
        model=Parent
        fields=('admission_no','father_name','mother_name','mothers_mobile_no','fathers_mobile_no','email')