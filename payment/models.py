
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import *
from student.models import Application
# Create your models here.

class Payment(models.Model):
    name=models.ForeignKey(Application,on_delete=models.CASCADE,blank=True,null=True)
    amount = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)
    payment_id=models.CharField(max_length=200,blank=True)
    order_id=models.CharField(max_length=20,blank=True)
    is_paid=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return str(self.name)

    # def save(self,*args,**kwargs):
    #     a=Payment.objects.all()
    #     for i in a:
    #         if self.is_paid == True:
    #             self.all_total=self.all_total+int(i.total_amount)        
    #         print(self.all_total)
    #     super().save(*args, **kwargs)