from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'mySchool/home.html')


def about(request):
    return render(request,'mySchool/about.html')

def payment(request):
    return render(request,'mySchool/payment.html')