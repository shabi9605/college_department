from django import forms
from django.forms.widgets import PasswordInput, Widget
from .models import *
from django.contrib.auth.models import User
from django.forms.widgets import NumberInput


class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Application
        fields=('landmark','district','mobile_no2','gender',
        'religion','cast','photo','course_name','course_name_previous_college',
        'management_or_community_status','appering_or_passout','persentage_obtained',)


class PreacdamicForm(forms.ModelForm):
    class Meta:
        model=PreacdemicDetails
        fields=('sslc_school_name','sslc_Persentage','sslc_passout_year','higher_secondary_school_name',
        'hss_persentage','hss_passout_year','college_name','course_name','college_passout_year',
        'year_gap','institution_last_studied')

class ApprovePreacdamicForm(forms.ModelForm):
    class Meta:
        model=PreacdemicDetails
        fields=('sslc_school_name','sslc_Persentage','sslc_passout_year','higher_secondary_school_name',
        'hss_persentage','hss_passout_year','college_name','course_name','college_passout_year',
        'year_gap','institution_last_studied','approve')

class ChalanForm(forms.ModelForm):
    dob=forms.DateField(required=True, widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model=ChalanGeneration
        fields=('purpose_of_this_chalan','student_name','register_no','address',
        'dob','mobile_no','email','amount',)

class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('complaint',)

class UpdateComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields=('complaint','replay')