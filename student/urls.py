from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('basic/',views.basic,name='basic'),
    path('basic_view/',views.basic_view,name='basic_view'),

    path('application/<int:id>',views.application,name='application'),
    path('application_view/',views.application_view,name='application_view'),
    path('all_applications/',views.all_applications,name='all_applications'),

    path('complaint/',views.complaint,name='complaint'),
    path('complaint_list/',views.complaint_view,name='complaint_list'),
    path('complaint_replay/<int:id>/',views.complaint_replay,name='complaint_replay'),
    path('complaint_replay_view/',views.complaint_replay_view,name='com_replay_view'),


    path('chalan/', views.chalan, name='chalan'),
    path('chalan_view/', views.chalanview, name='chalanview'),
    path('report/',views.report,name="report"),
    path('search_studentcom/',views.search_studentcom,name='search_studentcom'),


    path('preacadamic/',views.preacadamic,name='preacadamic'),
    path('preacdamic_view/', views.preacdamic_view, name='preacdamic_view'),
    path('preappruve/<int:id>',views.preappruve,name='preappruve'),
    path('preacdamicapp_view/', views.preacdamicapp_view, name='preacdamicapp_view'),
    path('search_pre/', views.search_pre, name='search_pre'),
    path('course_view2/<int:id>/', views.course_view2, name='course_view2'),

    path('student_details',views.student_details,name='student_details'),
    path('parent_details',views.parent_details,name='parent_details'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)