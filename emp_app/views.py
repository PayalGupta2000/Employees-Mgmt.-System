from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def view_all(request):
    emp=Employee.objects.all()
    return render(request,"view_all.html",{"emps":emp})

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=request.POST['salary']
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        bonus=int(request.POST['bonus'])
        new_emp=Employee(first_name=first_name, last_name=last_name,salary=salary,bonus=bonus,dept_id=dept,role_id=role,phone=phone)
        new_emp.save()
        return HttpResponse("Employee added sucessfully.")
        
    elif request.method=="Get":
        return render(request,"add_emp.html")

    else:
        return HttpResponse("An exception occured! Employee has not been added")
