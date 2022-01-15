from django.contrib import admin
from .models import *
# Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     list_display=['name','email','subject','message']

# admin.site.register(Contact,ContactAdmin)

admin.site.site_header='SMART DEPARTMENT ADMIN'

class StudentAdmin(admin.ModelAdmin):
    list_display=['user','name','course_name','photo',]

admin.site.register(Student,StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display=['user','name','job_type','photo']

admin.site.register(Teacher,TeacherAdmin)

class NonTeachingStaffAdmin(admin.ModelAdmin):
    list_display=['user','name','mobile_no','job_type']

admin.site.register(NonTeaching_Staff,NonTeachingStaffAdmin)

admin.site.register(Semester)

class CourseAdmin(admin.ModelAdmin):
    list_display=['course_name','description','no_of_semsters']

admin.site.register(Course,CourseAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display=['title','course','semster',]

admin.site.register(Subject,SubjectAdmin)


class SyllabusAdmin(admin.ModelAdmin):
    list_display=['name','course']

admin.site.register(Syllabus,SyllabusAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display=['title','notification','starting_date','ending_date']

admin.site.register(Notification,NotificationAdmin)


admin.site.register(Parent)
