from django.shortcuts import render
from .models import *
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
#from .serializer import
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def companies(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    companies = Company.objects.all()

    return render(request,'companies.html',{"companies":companies})

@login_required(login_url='/accounts/login/')
def make_user(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    makeusers=Make_users.objects.all()

    return render(request,'makeuserhtml',{"makeusers":makeusers})

@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('profile')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'profile.html',{"profile":profile, "form":form})