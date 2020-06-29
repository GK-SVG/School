from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
import datetime
#last commit changed
MERCHANT_KEY = 'MJs5tlGfwOMzMTQ@'
# Create your views here.
def home(request):
    return render(request,'mySchool/home.html')


def about(request):
    return render(request,'mySchool/about.html')

def addmission(request):
    return render(request,'mySchool/addmission.html')


def payment(request):
    return render(request,'mySchool/payment.html')

def processpayment(request):
    name=request.GET['name']
    roll=request.GET['roll']
    Class=request.GET['class']
    print(Class)
    father=request.GET['father']
    ammount=request.GET['ammount']
    student=Student.objects.get(rollNo=roll)
    transaction_id=datetime.datetime.now().timestamp()
    studentfee=StudentFees.objects.create(name=name,transaction_id=transaction_id,payment=ammount,roll=roll)
    studentfee.save()
    print(student.Class)
    if not student.name==name:
        messages.error(request,'Student name does not match')
        return redirect('/payment')
    if not student.father==father:
        messages.error(request,'Student father name does not match')
        return redirect('/payment')
    param_dict={
			    
				'MID': 'toaldV34834751882298',
                'ORDER_ID': str(transaction_id),
                'TXN_AMOUNT': str(ammount),
                'CUST_ID': roll,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
	}
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    return render(request,'mySchool/paytm.html',{'param_dict':param_dict})		
    
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order success full')
        else:
            #order_success=messages.error(request,f'order was not successful because {response_dict[RESPMSG]}')
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'mySchool/paymentstatus.html', {'response': response_dict})