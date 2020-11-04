from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import  CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from rest_framework.response import Response
from rest_framework.views import APIView
#from .serializer import
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='manager')
			user.groups.add(group)
			Manager.objects.create(
				user=user,
				name=user.username,
				)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, '', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def employee_profile_view(request):
	
  if request.method == 'POST':
		
    user_form = UserForm(request.POST, prefix='UF')
		profile_form = EmployeeProfileForm(request.POST, prefix='PF')
		
    if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			user.save()

			user.employee_profile.name = profile_form.cleaned_data.get('name')
			user.employee_profile.phone = profile_form.cleaned_data.get('phone')
            user.employee_profile.email = profile_form.cleaned_data.get('email')

			user.employee_profile.save()
			
	else:
		user_form = UserForm(prefix='UF')
		profile_form = EmployeeProfileForm(prefix='PF')
		
	return render(request, '',{
			
		})


def teamlead_profile_view(request):
	
  if request.method == 'POST':
		
    user_form = UserForm(request.POST, prefix='UF')
		profile_form = TeamLeadProfileForm(request.POST, prefix='PF')
		
    if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			user.save()

			user.teamlead_profile.team_name = profile_form.cleaned_data.get('team_name')
			user.teamlead_profile.website = profile_form.cleaned_data.get('website')
			user.teamlead_profile.save()
			
	else:
		user_form = UserForm(prefix='UF')
		profile_form = TeamLeadProfileForm(prefix='PF')
		
	return render(request, '',{
			'user_form': user_form,
			'profile_form': profile_form,
		})