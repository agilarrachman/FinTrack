from django.shortcuts import redirect, render
from .models import Income

def index(request):
    income=Income.objects.all()
    return render(request,'index.html',{'income':income})

def login(request):
    return render(request,'login.html')

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['tanggal']
    y=request.POST['jumlah']
    z=request.POST['deskripsi']
    income=Income(tanggal=x,jumlah=y,deskripsi=z)
    income.save()
    return redirect("/")

def delete(request,id):
    income=Income.objects.get(id=id)
    income.delete()
    return redirect("/")

def update(request,id):
    income=Income.objects.get(id=id)
    return render(request,'update.html',{'income':income})

def uprec(request,id):
    x=request.POST['tanggal']
    y=request.POST['jumlah']
    z=request.POST['deskripsi']
    income=Income.objects.get(id=id)
    income.tanggal=x
    income.jumlah=y
    income.deskripsi=z
    income.save()
    return redirect("/")
