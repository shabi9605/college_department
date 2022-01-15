from django.db.models.enums import TextChoices
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

def generate_rndm():
    digit_char = random.choices(string.ascii_uppercase, k=9) + random.choices(string.digits, k=2)
    random.shuffle(digit_char)
    return "NAA3U" + ''.join(digit_char)
# Create your views here.
def index(request):
    notifications=Notification.objects.filter(approve=True).order_by('-id')
    print(notifications)
    return render(request,'index.html',{'notifications':notifications})


# def contact(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         subject=request.POST.get('subject')
#         message=request.POST.get('message')
        
#         Contact.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message
#         )
#         return render(request,'contact.html',{'msg': 'Successfully sent message'})
#     return render(request,'contact.html')

def dashboard(request):
    t=Notification.objects.filter(approve=True)

    total_student=Student.objects.all().count()
    total_teacher=Teacher.objects.all().count()
    total_staff=NonTeaching_Staff.objects.all().count()
    total_course=Course.objects.all().count()
    context = {    
        'noti':t,
        'total_student':total_student,
        'total_teacher':total_teacher,
        'total_staff':total_staff, 
        'total_course':total_course   
    }
    return render(request,'dashboard/index.html',context)


def signin(request):
     if request.method=="POST":
          username=request.POST.get('username')
          password=request.POST.get('password')
          user=authenticate(username=username,password=password)
          if user:
               if user.is_active:
                    login(request,user)
                    return redirect('dashboard')
               else:
                    HttpResponse('not active')
          else:
               messages.error(request,'invalid username or password')
               return redirect('signin')
     return render(request,'index.html')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/')



def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"YOUR PASSWORD SUCCEFULLY UPDATED")
            return render(request,'account/change_password.html')
        else:
            messages.error(request,'PLEASE CORRECT ERROR')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'account/change_password.html',{'form':form})



def student_register(request):
    if request.method=='POST':
        # user_form=UserForm(request.POST)
        student_form=StudentForm(request.POST,request.FILES)
        # s=UserForm.username
        if student_form.is_valid():
            p=generate_rndm()
            u=random.randint(10000,100000)
            usernew = User.objects.create_user(
                username=student_form.cleaned_data['email'],
                password=p,
            )
            usernew.save()
            profile=student_form.save(commit=False)
            profile.user=usernew
            profile.admission_no=u
            profile.save()
            a=profile.email
         
            send_mail('Username:'+str(usernew.username),'Password:'+str(p),'shabi960580@gmail.com',[a])

            messages.success(request,'Thank You For Registering')
            return redirect('dashboard')

        else:
            HttpResponse('invalid form')
    else:
        # user_form=UserForm()
        student_form=StudentForm()
       
    return render(request,'admin/student_register.html',{'student_form':student_form})


def update_student_profile(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_student_form=StudentProfileForm(request.POST,request.FILES,instance=request.user.student)
        if update_form.is_valid() and update_student_form.is_valid():
            update_form.save()
            update_student_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_student_form=StudentProfileForm(instance=request.user.student)

    context={
        'update_form':update_form,
        'update_student_form':update_student_form
    }
    return render(request,'account/update_student_profile.html',context)


def teacher_register(request):
    if request.method=='POST':
        teacher_form=TeacherForm(request.POST,request.FILES)
        if  teacher_form.is_valid():
            p=generate_rndm()
            u=random.randint(10000,100000)
            usernew = User.objects.create_user(
                username=teacher_form.cleaned_data['email'],
                password=p,
            )
            usernew.save()
            profile=teacher_form.save(commit=False)
            profile.user=usernew
            profile.teacher_id=u
            profile.save()
            a=profile.email
            
            send_mail('Username:'+str(usernew.username),'Password:'+str(p),'shabi960580@gmail.com',[a])

            messages.success(request,'Thank You For Registering')
            return redirect('dashboard')

        else:
            HttpResponse('invalid form')
    else:
      
        teacher_form=TeacherForm()
       
    return render(request,'admin/teacher_register.html',{'teacher_form':teacher_form})








def parent_register(request):
    if request.method=='POST':
        teacher_form=ParentForm(request.POST,request.FILES)
        if  teacher_form.is_valid():
            p=generate_rndm()
            u=random.randint(10000,100000)
            usernew = User.objects.create_user(
                username=teacher_form.cleaned_data['email'],
                password=p,
            )
            usernew.save()
            profile=teacher_form.save(commit=False)
            profile.parent=usernew
            profile.father_name=teacher_form.cleaned_data['father_name']
            profile.mother_name=teacher_form.cleaned_data['mother_name']
            profile.mothers_mobile_no=teacher_form.cleaned_data['mothers_mobile_no']
            profile.fathers_mobile_no=teacher_form.cleaned_data['fathers_mobile_no']
            profile.email=teacher_form.cleaned_data['email']
            profile.save()
            a=profile.email
            
            send_mail('Username:'+str(usernew.username),'Password:'+str(p),'shabi960580@gmail.com',[a])

            messages.success(request,'Thank You For Registering')
            return redirect('dashboard')

        else:
            HttpResponse('invalid form')
    else:
      
        teacher_form=ParentForm()
       
    return render(request,'admin/parent_register.html',{'teacher_form':teacher_form})





def update_teacher_profile(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_teacher_form=TeacherProfileForm(request.POST,request.FILES,instance=request.user.teacher)
        if update_form.is_valid() and update_teacher_form.is_valid():
            update_form.save()
            update_teacher_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_teacher_form=TeacherProfileForm(instance=request.user.teacher)

    context={
        'update_form':update_form,
        'update_teacher_form':update_teacher_form
    }
    return render(request,'account/update_teacher_profile.html',context)

def staff_register(request):
    if request.method=='POST':
        staff_form=NonTeachingStaffForm(request.POST,request.FILES)

        if staff_form.is_valid():
            p=generate_rndm()
            u=random.randint(10000,100000)
            usernew = User.objects.create_user(
                username=staff_form.cleaned_data['email'],
                password=p,
            )
            usernew.save()
            profile=staff_form.save(commit=False)
            profile.user=usernew
            profile.staff_id=u
            profile.save()
            a=profile.email
            
            send_mail('Username:'+str(usernew.username),'Password:'+str(p),'shabi960580@gmail.com',[a])

            messages.success(request,'Thank You For Registering')
            return redirect('dashboard')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm2()
        staff_form=NonTeachingStaffForm()
       
    return render(request,'admin/staff_register.html',{'user_form':user_form,'staff_form':staff_form})


def update_staff_profile(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_staff_form=NonTeachingStaffPrfileForm(request.POST,request.FILES,instance=request.user.nonteaching_staff)
        if update_form.is_valid() and update_staff_form.is_valid():
            update_form.save()
            update_staff_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_staff_form=NonTeachingStaffPrfileForm(instance=request.user.nonteaching_staff)

    context={
        'update_form':update_form,
        'update_staff_form':update_staff_form
    }
    return render(request,'account/update_staff_profile.html',context)






# def add_feed_details(request):
#     if request.method=='POST':
#         form=AddFeedForm(request.POST,request.FILES)
#         if form.is_valid():
#             user=request.user
#             user.save()
#             m_form=form.save()
#             m_form.user=user
#             m_form.save()
#             messages.success(request,'successfully added')
#             return redirect('dashboard')
#         else:
#             HttpResponse('invalid form')
#     else:
#         form=AddFeedForm()
#     return render(request,'feed/add_feed.html',{'form':form,})
    

# def feed_details(request):
#     feed=Feed.objects.filter(user=request.user)
#     return render(request,'feed/feed_details.html',{'feed':feed})

# def update_feed(request,id):
#     Update = Feed.objects.get(id=id)
#     form= UpdateFeedForm(instance=Update)
#     if request.method=='POST':
#         form= UpdateFeedForm(request.POST,request.FILES,instance=Update)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Record Update succefully')
#             return redirect('dashboard')
#     return render(request,'feed/feed_update.html',{'form':form})

# def delete_feed_details(request,id):
#     deletef=Feed.objects.get(id=id)
#     deletef.delete()
#     return redirect('feed_details')

# def question(request):
#     q=Question.objects.all()
#     return render(request,'question/question.html',{'q':q})

# def search_q(request):
#     if request.method=='GET':
#         q=request.GET.get('query')
#         s=Question.objects.filter(question__icontains=q)|Question.objects.filter(answer__icontains=q)
#         print(s)
    
#     return render(request,'question/search_question.html',{'s':s})


# PDF GENEARATION 

   
# def ashaworkers(request):
#     a=Ashaworker.objects.all()
#     return render(request,'report/ashaworkers.html',{'a':a})


# def report_ashaworkers(request):
#     path = "pdf/asha_template.html"
#     context = {"asha" : Ashaworker.objects.all()[:100]}

#     html = render_to_string('pdf/asha_template.html',context)
#     io_bytes = BytesIO()
    
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)
    
#     if not pdf.err:
#         return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
#     else:
#         return HttpResponse("Error while rendering PDF", status=400)



# def co_positive(request):
#     dates=datetime.now()
#     print(dates)
#     day1=dates.date()+timedelta(days=-1)
#     print(day1)
#     context =  Covid.objects.all().filter(test_result='Postitive')
#     path = "pdf/asha_template.html"
#     context = {"posi" : Covid.objects.all().filter(test_result='Postitive')[:100]}

#     html = render_to_string('pdf/asha_template.html',context)
#     io_bytes = BytesIO()
    
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)
    
#     if not pdf.err:
#         return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
#     else:
#         return HttpResponse("Error while rendering PDF", status=400)




def view_notification(request):
    notification=Notification.objects.all().order_by('-id')
    print(notification)
    return render(request,'account/notification.html',{'notification':notification})




def admission_form_view(request):
    return render(request,'account/admission_form.html')



def chalan_view(request):
    chalans=ChalanGeneration.objects.all().order_by('-id')
    return render(request,'account/view_chalans.html',{'chalans':chalans})


def view_paid_application(request):
    applications=Application.objects.filter(paid=True)
    return render(request,'account/view_paid_applications.html',{'applications':applications})


def view_pre_academic_details(request):
    pre_academic_details=PreacdemicDetails.objects.all().order_by('-id')
    if request.method=="GET":
       
        name=request.GET.get('name')
        
        try:
            student=PreacdemicDetails.objects.filter(student__name__icontains=name)
            print(student)
            return render(request,'account/view_academic_details.html',{'student':student})
        except:
            pass
        
    return render(request,'account/view_academic_details.html',{'pre_academic_details':pre_academic_details})