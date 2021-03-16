from datetime import datetime, timezone

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from questions.models import Time


def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password=password)
        if user is not None:
            login(request,user)
            request.session['userid'] = user.id
            return render(request,"user/start.html")
        return render(request,"user/login.html",{"error":"nouser"})
    else:
        return render(request,"user/login.html")

def signupview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username,password = password,email =email)
        return redirect("login:login")
    else:
        return render(request,"user/signup.html")
def startview(request):
    userid = request.session.get('userid')
    user = User.objects.get(pk=userid)
    now = datetime.now(timezone.utc)
    time = Time(user=user,time=now)
    time.save()
    request.session['timeid'] = time.id
    return redirect("questions:questions",id=0)



