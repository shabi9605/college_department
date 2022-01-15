from django.contrib import messages
from django.db.models.fields import PositiveIntegerField

from .models import *
from django.shortcuts import render
import razorpay
from .forms import PaymentForm
from student.models import *


def payment(request,id):
    a=Application.objects.get(id=id)
    request.session['application']=id
    b=Application.objects.filter(course_name__id=a.course_name.id)
    t=a.course_name.admission_fee
    print(t)
    if request.method == "POST":
        # name = request.POST.get('name')
        amount1=request.POST.get('amount')
        t=int(amount1)
        amount = t *100
        client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
        response_payment = client.order.create(dict(amount=amount,
                                                    currency='INR')
                                               )

        order_id = response_payment['id']
        order_status = response_payment['status']
        
        if order_status == 'created':
            payment = Payment(
                name=a,
                amount=a.course_name,
                order_id=order_id,
                # total_amount=t,
                # user=request.user,
                
            )
          
        payment.save()
        
        
        response_payment['user'] = a.name
        form = PaymentForm(request.POST or None)
        return render(request, 'payment/payment.html', {'form':form,'payment': response_payment,'t':t,'name':a.name})

    form = PaymentForm()
    return render(request, 'payment/payment.html', {'form': form,'t':t,'name':a.name})


def payment_status(request):
   
    response = request.POST
    params_dict = {

       'razorpay_order_id': response['razorpay_order_id'],
       'razorpay_payment_id': response['razorpay_payment_id'],
       'razorpay_signature': response['razorpay_signature'],
     
    }

    # client instance
    client = razorpay.Client(auth=('rzp_test_48Z9LMTDVAN5JU', 'gMxfhwgZ73ANYJQCeblLMy7W'))
    

    try:
        status = client.utility.verify_payment_signature(params_dict)
        payment = Payment.objects.get(order_id=response['razorpay_order_id'])
        payment.payment_id = response['razorpay_payment_id']
        payment.is_paid = True
        payment.save()
        try:
            application=request.session['application']
            pay=Application.objects.get(id=application)
            print(pay.paid)
            requirement=Application.objects.update_or_create(id=application,
            defaults={'paid':True}
            )
            print(pay.paid)
        except:
            pass
        return render(request, 'payment/payment_status.html', {'status': True,'payment_id':payment.payment_id})
    except:
        return render(request, 'payment/payment_status.html', {'status': False})


def allpayments(request):
    payall=Payment.objects.all()
    return render(request,'payment/allpayment.html',{'payall':payall})

def userpaymentview(request):
    userpay=Payment.objects.filter(name__adhar_no=request.user.student.adhar_no)
    return render(request,'payment/userpayment.html',{'userpay':userpay})