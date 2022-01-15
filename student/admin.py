from django.contrib import admin
from .models import *
# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display=['name','course_name','photo','paid']

admin.site.register(Application,ApplicationAdmin)

class BasicAdmin(admin.ModelAdmin):
    list_display=['name','place','adhar_no','mobile_no']

admin.site.register(Basic_Details,BasicAdmin)

class PreacdamicAdmin(admin.ModelAdmin):
    list_display=['student','sslc_school_name','higher_secondary_school_name','course_name']

admin.site.register(PreacdemicDetails,PreacdamicAdmin)

class ComplaintAdmin(admin.ModelAdmin):
    list_display=['student','complaint','replay','created_date']

admin.site.register(Complaint,ComplaintAdmin)

class ChalanAdmin(admin.ModelAdmin):
    list_display=['student_name','register_no','email','mobile_no']

admin.site.register(ChalanGeneration,ChalanAdmin)