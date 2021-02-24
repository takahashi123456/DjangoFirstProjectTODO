from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import todoModel
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import todoForm

# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username,"",password)
            return redirect("login")
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


def taskfunc(request):
    if request.method =="POST":
        # todo = todoModel(title=request.POST["title"]) 
        # todo1 = todoModel(content=request.POST["content"])
        # todo2 = todoModel(author=request.POST["author"])
        # todo3 = todoModel(dateline=request.POST["dateline"])
        # todo4 = todoModel(now_date=timezone.datetime.today())
        # todo5 = todoModel(priority=request.POST["priority"])
        obj = todoModel()
        todo = todoForm(request.POST, instance=obj)
        todo.save()

        return redirect("list")
        # except:
        #     return render(request,"list.html",{"error":"このTODOは登録されています。"})
        # todo = todoModel(text=request.POST['text'])
        # todo.save()
        
    return render(request, "task.html",{})

# class taskfuncCreate(CreateView):
#     template_name = "task.html"
#     model = todoModel
#     fields = ("title", "content","author","priority")
#     success_url = reverse_lazy("list")
