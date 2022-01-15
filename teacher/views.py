from typing import Iterator
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
import random
from account.models import *
from account.forms import *
# Create your views here.

def table_details(request):
    t=TimeTable.objects.all()
    return render(request,'timetable/table_details.html',{'t':t})

def aptablestudent(request):
    t=TimeTable.objects.filter(appruve=True,course=request.user.student.course_name,semster=request.user.student.semster)
    return render(request,'timetable/aptable_details.html',{'t':t})

def aptablesteacher(request):
    t=TimeTable.objects.filter(appruve=True,)
    return render(request,'timetable/tetable_details.html',{'t':t})

def update_table(request,id):
    Update = TimeTable.objects.get(id=id)
    form= TimetableForm(instance=Update)
    if request.method=='POST':
        form= TimetableForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('table_details')
    return render(request,'timetable/table_update.html',{'form':form})

def delete_table_details(request,id):
    deletef=TimeTable.objects.get(id=id)
    deletef.delete()
    return redirect('table_details') 


def noti_details(request):
    t=Notification.objects.all()
    return render(request,'noti/noti_details.html',{'t':t})

# def apnoti(request):
#     t=Notification.objects.filter(approve=True)
#     return render(request,'noti/apnoti_details.html',{'t':t})

def update_noti(request,id):
    Update = Notification.objects.get(id=id)
    form= NotificationForm(instance=Update)
    if request.method=='POST':
        form= NotificationForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('noti_details')
    return render(request,'noti/noti_update.html',{'form':form})

def delete_noti_details(request,id):
    deletef=Notification.objects.get(id=id)
    deletef.delete()
    return redirect('table_details') 


def addav(request):
   
    if request.method=='POST':
        form=AvForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            user.save()
            m_form=form.save()
            
            m_form.user=user
            
            m_form.save()
            messages.success(request,'successfully added')
            return redirect('av_details')
        else:
            HttpResponse('invalid form')
    else:
        form=AvForm()
    return render(request,'av/add_av.html',{'form':form,})


def av_details(request):
    t=Audio_Video.objects.filter(user=request.user)
    adv=Audio_Video.objects.all().order_by('-id')
    return render(request,'av/av_details.html',{'t':t,'t':adv})

def update_av(request,id):
    Update = Audio_Video.objects.get(id=id)
    form= AvForm(instance=Update)
    if request.method=='POST':
        form= AvForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('av_details')
    return render(request,'av/av_update.html',{'form':form})

def delete_av_details(request,id):
    deletef=Audio_Video.objects.get(id=id)
    deletef.delete()
    return redirect('av_details') 

def course_view(request,id):
    c=Course.objects.get(id=id)
    s=Student.objects.filter(course_name=c)
    return render(request,'internals/students.html',{'s':s})



def all_studnet(request):
    b=Course.objects.all()
    s=Student.objects.all()
    sem=Semester.objects.all()
    return render(request,'internals/students.html',{'s':s,'b':b,'sem':sem})

def addinternal(request,id):
    s=Student.objects.get(id=id)
    if request.method=='POST':
        form=InternalMarkForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user.teacher
            user.save()
            m_form=form.save()        
            m_form.user=user   
            m_form.student=s         
            m_form.save()
            messages.success(request,'successfully added')
            return redirect('internal_details')
        else:
            HttpResponse('invalid form')
    else:
        form=InternalMarkForm()
    return render(request,'internals/internals.html',{'form':form,})

def internal_detailsstu(request):
    b=Semester.objects.all()
    print(b)
    try:
        print(request.user.parent.admission_no)
    except:
        pass
    try:

        t=InternalMark.objects.filter(student=request.user.student)
    except:
        t=InternalMark.objects.filter(student=request.user.parent.admission_no)
    print(t)
    return render(request,'internals/stinternal_details.html',{'t':t,'b':b})



def attendance_detailsstu(request):
    b=Semester.objects.all()
    print(b)
    try:
        print(request.user.parent.admission_no)
    except:
        pass
    try:

        t=InternalMark.objects.filter(student=request.user.student)
    except:
        t=InternalMark.objects.filter(student=request.user.parent.admission_no)
    print(t)
    return render(request,'internals/stattendance_details.html',{'t':t,'b':b})

def internal_currentsem(request,id):
    b=InternalMark.objects.get(id=id)
    t=InternalMark.objects.filter(student=request.user.student,semster=request.user.student.semster)
    return render(request,'internals/seminternal_details.html',{'t':t,'b':b})

def internal_currentsem(request,id):
    sub=Subject.objects.all()
    t=InternalMark.objects.filter(student=request.user.student,subject__course=request.user.student.course_name)
    return render(request,'internals/seminternal_details.html',{'t':t})


def internal_details(request):
    t=InternalMark.objects.filter(user=request.user.teacher)
    return render(request,'internals/internal_details.html',{'t':t})

def update_internal(request,id):
    Update = InternalMark.objects.get(id=id)
    form= UpdateInternalMarkForm(instance=Update)
    if request.method=='POST':
        form= UpdateInternalMarkForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('internal_details')
    return render(request,'internals/internal_update.html',{'form':form})

def delete_internal_details(request,id):
    deletef=InternalMark.objects.get(id=id)
    deletef.delete()
    return redirect('internal_details') 

def search_internal(request):
    if request.method=='GET':
        q=request.GET.get('query')
        s=Student.objects.filter(name__icontains=q)|Student.objects.filter(admission_no__icontains=q)
        return render(request,'internals/students.html',{'s':s})
    return render(request,'internals/students.html')


def search_internal_sem(request):
    
    if request.method=='GET':
        q=request.GET.get('query')
        s=Student.objects.filter(semster__title__icontains=q)
        return render(request,'internals/students.html',{'s':s})
    return render(request,'internals/students.html')
    

def course_view1(request,id):
    c=Course.objects.get(id=id)
    s=Student.objects.filter(course_name=c)
    return render(request,'assignment/students.html',{'s':s})

def all_studnet1(request):
    b=Course.objects.all()
    s=Student.objects.all()
    return render(request,'assignment/students.html',{'s':s,'b':b})

def addassignments(request,id):
    s=Student.objects.get(id=id)
    if request.method=='POST':
        form=AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            user=request.user
            user.save()
            m_form=form.save()        
            m_form.user=user   
            # m_form.student=s         
            m_form.save()
            messages.success(request,'successfully added')
            return redirect('assignment_details')
        else:
            HttpResponse('invalid form')
    else:
        form=AssignmentForm()
    return render(request,'assignment/assignment.html',{'form':form,})

def search_assignment(request):
    if request.method=='GET':
        q=request.GET.get('query')
        s=Student.objects.filter(name__icontains=q)|Student.objects.filter(admission_no__icontains=q)
        return render(request,'assignment/students.html',{'s':s})
    return render(request,'assignment/students.html')

def assignment_details(request):
    t=Assignment.objects.filter(user=request.user)
    return render(request,'assignment/assignment_details.html',{'t':t})



def search_assignment_sem(request):
    if request.method=='GET':
        q=request.GET.get('query')
        s=Student.objects.filter(semster__title__icontains=q)
        return render(request,'assignment/students.html',{'s':s})
    return render(request,'assignment/students.html')

def update_assignment(request,id):
    Update = Assignment.objects.get(id=id)
    form= UpdateAssignmentForm(instance=Update)
    if request.method=='POST':
        form= UpdateAssignmentForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('assignment_details')
    return render(request,'assignment/assignment_update.html',{'form':form})

def delete_assignment_details(request,id):
    deletef=Assignment.objects.get(id=id)
    deletef.delete()
    return redirect('assignment_details') 




def all_teacher(request):
    all_teachers=Teacher.objects.filter(job_type='teacher',confirmation='not_confirmed')
    print(all_teachers)
    return render(request,'internals/teachers.html',{'all_teachers':all_teachers})


def confirm_teacher(request,id):
    teacher=Teacher.objects.get(id=id)
    print(teacher)
    form= HodUpdateTeacherForm(instance=teacher)
    if request.method=='POST':
        form= HodUpdateTeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return redirect('all_teacher')
    return render(request,'internals/confirm_teacher_edit.html',{'form':form})



def view_all_course(request):
    all_course=Course.objects.all().order_by('-id')
    print(all_course)
    return render(request,'internals/all_courses.html',{'all_course':all_course})



def manage_course(request,id):
    course=Course.objects.get(id=id)
    print(course)
    update_course_form=UpdateCourse(instance=course)
    if request.method=="POST":
        update_course_form=UpdateCourse(request.POST,request.FILES,instance=course)
        update_course_form.save()
        return redirect('view_all_course')
    return render(request,'internals/update_course.html',{'form':update_course_form})



def teacher_profile(request):
    profile=Teacher.objects.filter(user=request.user)
    return render(request,'account/teacher_profile.html',{'profile':profile})






def view_assignments(request):
    assignments=Assignment.objects.filter(course=request.user.student.course_name,answer=None)
    return render(request,'assignment/view_assignments.html',{'assignments':assignments})



def submit_assignments(request,id):
    assignment=Assignment.objects.get(id=id)
    print(assignment.title)

    if request.method=="POST":
        assignemnt_form=SubmitAssignment(request.POST,request.FILES)
        if assignemnt_form.is_valid():
            
            cp=Assignment(user=request.user,title=assignment.title,description=assignment.description,
            question=assignment.question,answer=assignemnt_form.cleaned_data['answer'],
            semster=assignment.semster,course=assignment.course)
            cp.save()

            
            return redirect('view_assignments')
        else:
            return HttpResponse("Invalid form")
    assignemnt_form=SubmitAssignment()
    return render(request,'assignment/assignment.html',{'form':assignemnt_form})




def view_submitted_assignments(request):
    assignments=Assignment.objects.filter(answer__isnull=False).order_by('-id')
    return render(request,'assignment/view_submitted_assignments.html',{'assignments':assignments})




def view_student_details(request):
    student_details=Student.objects.all().order_by('-id')
    print(student_details)
    if request.method=="GET":
       
        name=request.GET.get('name')
        
        try:
            student=Student.objects.filter(semster__title__icontains=name)
            print(student)
            return render(request,'account/view_stuent_details.html',{'student':student})
        except:
            pass
        
    return render(request,'account/view_stuent_details.html',{'student_details':student_details})




def view_all_attendance(request):
    
    t=InternalMark.objects.all().order_by('-id')
    
    print(t)
    return render(request,'internals/stattendance_details.html',{'t':t})