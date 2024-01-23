from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from .forms import BookingForm

# Create your views here.

# Create your views here.
# def index(request):
#     return HttpResponse("hello world")
# def about(request):
#     return HttpResponse("about page")
# def booking(request):
#     return HttpResponse("booking page")
# def contact (request):
#     return HttpResponse("contact page")
# def department(request):
#     return HttpResponse("department page")




def index(request):
    return render(request,"index.html",)

def about(request):
    return render(request,"about.html")

def booking(request):
    return render(request,"booking.html")

def contact(request):
    return render(request,"contact.html")

def department(request):
    return render(request,"department.html")

def Doctor(request):
    return render(request,"doctor.html")


def index(request):
    person={
        "name":"jhon",
        'age':20
    }
    numbers={
        'num1':[3,7,8,9,5,3]
        
    }
    return render(request,"index.html",numbers)
def department(request):
    dict_dep={
        'dept' :Department.objects.all()
    }
    return render(request, 'department.html',dict_dep)
def doctors(request):
    doct_dep={
        'doc'  :Doctors.objects.all()
    }
    return render(request, 'doctor.html',doct_dep)

def booking(request):
    if request.method =='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm 
    dict_form={
        "form":form
    }
    return render(request,"booking.html",dict_form)

 