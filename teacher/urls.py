from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

    path('table_details/',views.table_details,name='table_details'),
    path('update_table/<int:id>/',views.update_table,name='update_table'),
    path('delete_table_details/<int:id>/',views.delete_table_details,name='delete_table_details'),
    path('aptablestudent/',views.aptablestudent,name='aptablestudent'),
    path('aptablesteacher/',views.aptablesteacher,name='aptablesteacher'),

    path('noti_details/',views.noti_details,name='noti_details'),
    path('update_noti/<int:id>/',views.update_noti,name='update_noti'),
    path('delete_noti_details/<int:id>/',views.delete_noti_details,name='delete_noti_details'),
    # path('apnoti/',views.apnoti,name='apnoti'),

    path('addav/',views.addav,name='addav'),
    path('av_details/',views.av_details,name='av_details'),
    path('update_av/<int:id>/',views.update_av,name='update_av'),
    path('delete_av_details/<int:id>/',views.delete_av_details,name='delete_av_details'),
    
    path('all_studnet/',views.all_studnet,name='all_studnet'),
    path('search_internal/',views.search_internal,name='search_internal'),

    path('addinternal/<int:id>',views.addinternal,name='addinternal'),
    path('internal_details/',views.internal_details,name='internal_details'),
    path('update_internal/<int:id>/',views.update_internal,name='update_internal'),
    path('delete_internal_details/<int:id>/',views.delete_internal_details,name='delete_internal_details'),
    path('internal_detailsstu/',views.internal_detailsstu,name='internal_detailsstu'),
    path('internal_currentsem/<int:id>/',views.internal_currentsem,name='internal_currentsem'),

    path('all_studnet1/',views.all_studnet1,name='all_studnet1'),
    path('search_assignment/',views.search_assignment,name='search_assignment'),

    path('attendance_detailsstu',views.attendance_detailsstu,name='attendance_detailsstu'),

    path('teacher_profile',views.teacher_profile,name='teacher_profile'),
    path('view_assignments',views.view_assignments,name='view_assignments'),
    path('submit_assignments/<int:id>',views.submit_assignments,name='submit_assignments'),

    path('view_submitted_assignments',views.view_submitted_assignments,name='view_submitted_assignments'),


    path('all_teacher',views.all_teacher,name='all_teacher'),
    path('confirm_teacher/<int:id>/',views.confirm_teacher,name='confirm_teacher'),

    path('addassignments/<int:id>',views.addassignments,name='addassignments'),
    path('assignment_details/',views.assignment_details,name='assignment_details'),
    path('update_assignment/<int:id>/',views.update_assignment,name='update_assignment'),
    path('delete_assignment_details/<int:id>/',views.delete_assignment_details,name='delete_assignment_details'),
    
    path('course_view/<int:id>/',views.course_view,name='course_view'),
    path('course_view1/<int:id>/',views.course_view1,name='course_view1'),

    path('search_internal_sem/',views.search_internal_sem,name='search_internal_sem'),
    path('search_assignment_sem/',views.search_assignment_sem,name='search_assignment_sem'),



    path('view_all_course',views.view_all_course,name='view_all_course'),

    path('manage_course/<int:id>',views.manage_course,name='manage_course'),

    path('view_student_details',views.view_student_details,name='view_student_details'),

    path('view_all_attendance',views.view_all_attendance,name='view_all_attendance'),



    

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)