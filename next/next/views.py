from django.shortcuts import render , redirect, get_object_or_404

def viewfunc(request):
    return render(request, "espo.html",{})


def topfunc(request):
    return render(request, "top.html",{})