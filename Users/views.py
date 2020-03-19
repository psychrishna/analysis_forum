from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def Login_User(request):
    return HttpResponse("LOGIN PAGE")

def Logout_User(request):
    return HttpResponse("LOGOUT PAGE")

def Register_User(request):
    return HttpResponse("REGISTER PAGE")

    