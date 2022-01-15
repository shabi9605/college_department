from django.shortcuts import render,redirect
from django.utils import html
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
# from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from datetime import datetime ,timedelta
from django.http import FileResponse
# from fpdf import FPDF
from student.models import *
import random
import string
# Create your views here.


def add_ebook(request):
    if request.method=='POST':
        form=EbookForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            user.save()
            m_form=form.save()
            m_form.user=user
            m_form.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        form=EbookForm()
    return render(request,'ebook/add_ebook.html',{'form':form,})

def ebook_details(request):
    ebooks=Ebook.objects.filter(user=request.user)
    all_ebooks=Ebook.objects.all().order_by('-id')
    return render(request,'ebook/ebook_details.html',{'ebooks':ebooks,'ebooks':all_ebooks})

def update_ebook(request,id):
    Update = Ebook.objects.get(id=id)
    form= UpdateEbookForm(instance=Update)
    if request.method=='POST':
        form= UpdateEbookForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('ebook_details')
    return render(request,'ebook/ebook_update.html',{'form':form})

def delete_ebook_details(request,id):
    deletef=Ebook.objects.get(id=id)
    deletef.delete()
    return redirect('ebook_details')   

#book section 

def search_student(request):
    if request.method=='GET':
        q=request.GET.get('query')
        s=Student.objects.filter(admission_no__icontains=q)|Student.objects.filter(name__icontains=q)
        print(s)
    return render(request,'student/search_student.html',{'s':s})

def studentbook(request):
    s=Student.objects.all()
    return render(request,'book/students.html',{'s':s})

def search_studentbook(request):
    if request.method=='GET':
        q=request.GET.get('query')
        s=Student.objects.filter(admission_no__icontains=q)|Student.objects.filter(name__icontains=q)
        print(s)
        return render(request,'book/students.html',{'s':s})
    return render(request,'book/students.html')

def search_ebook(request):
    if request.method=='GET':
        q=request.GET.get('query')
        ebooks=Ebook.objects.filter(book_name__icontains=q)|Ebook.objects.filter(author__icontains=q)
        return render(request,'ebook/ebook_details.html',{'ebooks':ebooks})
    return render(request,'ebook/ebook_details.html')

def addstudentbook(request,id):
    s=Student.objects.get(id=id)
    print(s.id)
    if request.method=='POST':
        form=StudentbookForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            user.save()
            m_form=form.save()
            m_form.student=s
            m_form.user=user
            
            m_form.save()
            messages.success(request,'successfully added')
            return redirect('book_details')
        else:
            HttpResponse('invalid form')
    else:
        form=StudentbookForm()
    return render(request,'book/add_book.html',{'form':form,})

def book_details(request):
    books=StudentBook.objects.all().order_by('created_date')
    return render(request,'book/book_details.html',{'books':books})

def update_book(request,id):
    Update = StudentBook.objects.get(id=id)
    form= UpdateStudentbookForm(instance=Update)
    if request.method=='POST':
        form= UpdateStudentbookForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('book_details')
    return render(request,'book/book_update.html',{'form':form})

def delete_book_details(request,id):
    deletef=StudentBook.objects.get(id=id)
    deletef.delete()
    return redirect('book_details') 


def view_library_detail(request):
    student_library=StudentBook.objects.filter(student=request.user.student)
    print(student_library)
    return render(request,'book/student_library.html',{'student_library':student_library})




def staff_profile(request):
    profile=NonTeaching_Staff.objects.filter(user=request.user)
    return render(request,'account/staff_profile.html',{'profile':profile})