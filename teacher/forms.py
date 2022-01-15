from django import forms
from django.db.models import fields
from django.forms.widgets import PasswordInput, Widget
from .models import *
from django.contrib.auth.models import User
from account.models import *

class TimetableForm(forms.ModelForm):
    class Meta:
        model=TimeTable
        fields=('title','day','course','semster',
        'subject1','subject2','subject3','subject4','subject5',
        'subject6','appruve',)

class NotificationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields=('title','notification','notification_publish_date','starting_date',
        'ending_date','notification_type','course','semster','link',
        'file','approve',)

class AvForm(forms.ModelForm):
    class Meta:
        model=Audio_Video
        fields=('title','subject','description','audio',
        'video','link',)


class InternalMarkForm(forms.ModelForm):
    class Meta:
        model=InternalMark
        fields=('semster','course','subject',
        'test1_mark','test2_mark','seminar_mark','attendence','no_of_working_days',
        'attendence_mark','total_seminar_mark','total_internal_mark','final_total_internal_mark')

class UpdateInternalMarkForm(forms.ModelForm):
    class Meta:
        model=InternalMark
        fields=('semster','course','subject',
        'test1_mark','test2_mark','seminar_mark','attendence','no_of_working_days',
        'attendence_mark','total_seminar_mark','total_internal_mark','final_total_internal_mark')

class AssignmentForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('semster','course','title','description','question',)

class UpdateAssignmentForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('semster','title','description','question',)



class UpdateCourse(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'



class SubmitAssignment(forms.ModelForm):
    class Meta:
        model=Assignment
        fields=('answer',)