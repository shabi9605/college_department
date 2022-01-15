from django.contrib import admin
from .models import *
# Register your models here.
class StudentBookAdmin(admin.ModelAdmin):
    list_display=['user','student','book_name','author','return_date']
admin.site.register(StudentBook,StudentBookAdmin)

class EbookAdmin(admin.ModelAdmin):
    list_display=['book_name','author','link']

admin.site.register(Ebook,EbookAdmin)