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
from fpdf import FPDF
import random

from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa

# Create your views here.
def basic(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        adhar_no=request.POST.get('adhar_no')
        mobile_no=request.POST.get('mobile_no')
        dob=request.POST.get('dob')
        house_name=request.POST.get('house_name')
        place=request.POST.get('place')
        pincode=request.POST.get('pincode')
        a=random.randint(10000,100000)
        b=Basic_Details.objects.create(
            name=name,
            email=email,
            adhar_no=adhar_no,
            mobile_no=mobile_no,
            dob=dob,
            house_name=house_name,
            place=place,
            pincode=pincode,
            application_id=a
        )
        b.save()
        messages.success(request,'successfully added')
        return render(request,'application/basic.html',{'a':a})
    return render(request,'index.html')

def basic_view(request):
    if request.method=='POST':
        application_id=request.POST.get('application_id')
    n=Basic_Details.objects.filter(application_id=application_id)
    print(n)
    return render(request,'application/basic.html',{'n':n})

def application(request,id):
    n=Basic_Details.objects.get(id=id)
    if request.method=='POST':
        form=ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            a_form=form.save()
            a_form.name=n
            a_form.application_id=n.application_id
            a_form.save()
            f=Application.objects.filter(id=a_form.id)
            messages.success(request,'successfully application added')
            return render(request,'application/application.html',{'f':f})

        else:
            HttpResponse('invalid form')
    else:
        form=ApplicationForm()
    return render(request,'application/application.html',{'form':form})

def application_view(request):
    a=Application.objects.filter(name__adhar_no=request.user.student.adhar_no)
    return render(request,'student/application_view.html',{'a':a})


def all_applications(request):
    all=Application.objects.all()
    return render(request,'application/all_application.html',{'all':all})

#complaint

def complaint(request):
    if request.method=='POST':
        form=ComplaintForm(request.POST)
        if form.is_valid():
            user=request.user.student
            user.save()
            p_form=form.save()
            p_form.student=user
            p_form.save()
            messages.success(request,'successfully added')
            return redirect('com_replay_view')
        else:
            HttpResponse('invalid form')
    else:
        form=ComplaintForm()
    return render(request,'complaint/complaint.html',{'form':form})

def complaint_view(request):
    com=Complaint.objects.all()
    return render(request,'complaint/complaint_list.html',{'com':com})

def search_studentcom(request):
    if request.method=='GET':
        q=request.GET.get('query')
        s=Student.objects.filter(admission_no__icontains=q)|Student.objects.filter(name__icontains=q)
        print(s)
        return render(request,'complaint/complaint_list.html',{'com':s})
    return render(request,'complaint/complaint_list.html')

def complaint_replay_view(request):
    com=Complaint.objects.filter(student=request.user.student)
    return render(request,'complaint/replay_view.html',{'com':com})

def complaint_replay(request,id):
    Update = Complaint.objects.get(id=id)
    print(Update)
    form= UpdateComplaintForm(instance=Update)
    if request.method=='POST':
        form= UpdateComplaintForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Replay succefully')
            return redirect('complaint_list')
    return render(request,'complaint/complaint_replay.html',{'form':form,})

#chalan

def chalan(request):
    if request.method=='POST':
        form=ChalanForm(request.POST)
        if form.is_valid():   
            p_form=form.save()
            p_form.chalan_no=random.randint(10000,100000)
            p_form.user=request.user
            p_form.save()
            messages.success(request,'successfully generated')
            return redirect('chalanview')
        else:
            HttpResponse('invalid form')
    else:
        form=ChalanForm()
    return render(request,'chalan/chalan.html',{'form':form})

def chalanview(request):
    c=ChalanGeneration.objects.filter(user=request.user)
    return render(request,'chalan/chalan_view.html',{'c':c})
 
def report(request):
    path = "pdf/chalan_template.html"
    context = {"states" : ChalanGeneration.objects.filter(user=request.user)[:100]}

    html = render_to_string('pdf/chalan_template.html',context)
    io_bytes = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)
    
    if not pdf.err:
        return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error while rendering PDF", status=400)

def preacadamic(request):
    p=PreacdemicDetails.objects.filter(user=request.user)
    if p:
        messages.success(request,'Already Addded your Details Please Check appruval Status')
        return redirect('preacdamic_view')
    else:

        if request.method=='POST':
            form=PreacdamicForm(request.POST)
            if form.is_valid():
                user=request.user
                user.save()
                p_form=form.save()
                p_form.user=user
                p_form.student=request.user.student
                p_form.save()
                messages.success(request,'successfully added')
                return redirect('preacdamic_view')
            else:
                HttpResponse('invalid form')
        else:
            form=PreacdamicForm()
        return render(request,'preacadamic/preacadamic.html',{'form':form})
    return render(request,'preacadamic/preacadamic.html',)


def search_pre(request):
    if request.method=='GET':
        q=request.GET.get('query')
        s=PreacdemicDetails.objects.filter(student__name__icontains=q)|PreacdemicDetails.objects.filter(student__admission_no__icontains=q)
        return render(request,'preacadamic/preap_list.html',{'a':s})
    return render(request,'preacadamic/preap_list.html')

def preacdamic_view(request):
    
    p=PreacdemicDetails.objects.filter(user=request.user)
    a=PreacdemicDetails.objects.filter(approve=False)
    return render(request,'preacadamic/pre_list.html',{'pre':p,'a':a,})

def preacdamicapp_view(request):
    b=Course.objects.all()
    a=PreacdemicDetails.objects.all()
    return render(request,'preacadamic/preap_list.html',{'a':a,'b':b})

def course_view2(request,id):
    c=Course.objects.get(id=id)
    a=PreacdemicDetails.objects.filter(student__course_name=c)
    return render(request,'preacadamic/preap_list.html',{'a':a})

def preappruve(request,id):
    Update = PreacdemicDetails.objects.get(id=id)
    print(Update)
    form= ApprovePreacdamicForm(instance=Update)
    if request.method=='POST':
        form= ApprovePreacdamicForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'appruved succefully')
            return redirect('preacdamicapp_view')
    return render(request,'preacadamic/pre_approve.html',{'form':form,})





def student_details(request):
    try:
        print(request.user.parent.admission_no.user)
    except:
        pass
    try:
        t=Student.objects.filter(user=request.user.parent.admission_no.user)
        
    except:
        t=Student.objects.filter(user=request.user)#|filter(parent_name__icontains=request.user.parent.mother_name)
    print(t)
    return render(request,'student/student_details.html',{'t':t})




def parent_details(request):
    parent=Parent.objects.filter(parent=request.user)
    return render(request,'account/parent_details.html',{'parent':parent})