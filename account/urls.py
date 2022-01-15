from os import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index,name='index'),
    # path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),

    path('student_register/',views.student_register,name='student_register'),
    path('update_student_profile/',views.update_student_profile,name='update_student_profile'),

    path('teacher_register/',views.teacher_register,name='teacher_register'),
    path('update_teacher_profile/',views.update_teacher_profile,name='update_teacher_profile'),

    path('staff_register/',views.staff_register,name='staff_register'),
    path('update_staff_profile/',views.update_staff_profile,name='update_staff_profile'),


    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    
    path('password/',views.change_password,name="change_password"),

    
    path('view_notification',views.view_notification,name='view_notification'),
    
    path('parent_register',views.parent_register,name='parent_register'),


    path('admission_form_view',views.admission_form_view,name='admission_form_view'),

    path('chalan_view',views.chalan_view,name='chalan_view'),

    path('view_paid_application',views.view_paid_application,name='view_paid_application'),

    path('view_pre_academic_details',views.view_pre_academic_details,name='view_pre_academic_details'),
    
   

    

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)