from django import forms
from django.forms.widgets import PasswordInput, Widget
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import NumberInput

class StudentbookForm(forms.ModelForm):
    issue_date=forms.DateField(required=True, widget=NumberInput(attrs={'type':'date'}),)
    due_date=forms.DateField(required=True, widget=NumberInput(attrs={'type':'date'}))
    return_date=forms.DateField(required=True, widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model=StudentBook
        fields=('year_of_admission','book_name','edition','author','issue_date',
        'due_date','return_date')

class UpdateStudentbookForm(forms.ModelForm):
    issue_date=forms.DateField(required=True, widget=NumberInput(attrs={'type':'date'}),)
    due_date=forms.DateField(required=True, widget=NumberInput(attrs={'type':'date'}))
    return_date=forms.DateField(required=True, widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model=StudentBook
        fields=('year_of_admission','book_name','edition','author','issue_date',
        'due_date','return_date')


class EbookForm(forms.ModelForm):
    class Meta:
        model=Ebook
        fields=('book_name','author','book_file','link','author',)

class UpdateEbookForm(forms.ModelForm):
    class Meta:
        model=Ebook
        fields=('book_name','author','book_file','link','author',)



