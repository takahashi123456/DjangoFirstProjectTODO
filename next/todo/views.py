from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import todoModel
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username,"",password)
            return render(request,"signup.html",{})
        except:
            return render(request,"signup.html",{"error":"このユーザーは登録されています。"})
    return render(request, "signup.html",{})


def loginfunc(request):
    if request.method == "POST":
        john = request.POST["username"]
        secret = request.POST["password"]
        user = authenticate(request,username=john, password=secret)
        if user is not None:
            login(request, user)
            return redirect("list")
    # A backend authenticated the credentials
        else:
            return render(request,"login.html",{"error":"ログインに失敗しました。"})
    # No backend authenticated the credentials
    return render(request, "login.html",{})
@login_required
def listfunc(request):
    todoModels = {'todo': todoModel.objects.all()}

    return render(request,'list.html',todoModels)
@login_required
def detailfunc(request,pk):
    # todoModels = {'todo': todoModel.objects.get(pk=pk)}

    # return render(request,'list.html',todoModels)
    todoModels = todoModel.objects.get(pk=pk)
    return render(request,'detail.html',{"todoModels":todoModels})


# def taskfunc(request):
    
