from django.contrib import admin
from .models import *
# Register your models here.
class TimeTableAdmin(admin.ModelAdmin):
    list_display=['title','semster','course','day','appruve']

admin.site.register(TimeTable,TimeTableAdmin)

class AudioVideoAdmin(admin.ModelAdmin):
    list_display=['user','title','subject','audio','video',]

admin.site.register(Audio_Video,AudioVideoAdmin)

class AssignmentlAdmin(admin.ModelAdmin):
    list_display=['user','semster','course',]

admin.site.register(Assignment,AssignmentlAdmin)

class InernalAdmin(admin.ModelAdmin):
    list_display=['student','semster','course','subject','total_internal_mark']

admin.site.register(InternalMark,InernalAdmin)