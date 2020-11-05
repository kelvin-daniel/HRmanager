from django.shortcuts import render, redirect, get_object_or_404
from .models import Leave
from .forms import LeaveCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializer import
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib import messages



# Create your views here.



def leave_creation(request):
	if not request.user.is_authenticated:
		return redirect('accounts:login')
	if request.method == 'POST':
		form = LeaveCreationForm(data = request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			user = request.user
			instance.user = user
			instance.save()


			
			messages.success(request,'Leave Request Sent,wait for Human Resource Managers response',extra_tags = 'alert alert-success alert-dismissible show')
			return redirect('createleave')

		messages.error(request,'failed to Request a Leave,please check entry dates',extra_tags = 'alert alert-warning alert-dismissible show')
		return redirect('createleave')


	dataset = dict()
	form = LeaveCreationForm()
	dataset['form'] = form
	dataset['title'] = 'Apply for Leave'
	return render(request,'leaves/create_leave.html',dataset)

# def leave_creation(request):
# 	current_user = request.user
	
# 	if request.method == 'POST':
# 		form = LeaveCreationForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance = form.save(commit = False)
# 			instance.user = current_user
# 			instance.save()
# 		return redirect('createleave')
# 	else:
#         form = LeaveCreationForm()
# 		return render(request,'leaves/create_leave.html', {"form":form})



def leaves_list(request):
	if not (request.user.is_staff and request.user.is_superuser):
		return redirect('/')
	leaves = Leave.objects.all()
	return render(request,'leaves/leaves_recent.html',{'leave_list':leaves,'title':'leaves list'})




def leaves_view(request,id):
	current_user = request.user
#connect to the registered employees
	leave = get_object_or_404(Leave, id = id)
	employee = Employee.objects.filter(user = leave.user)[0]
	print(employee)
	return render(request,'leaves/leave_detail_view.html',{'leave':leave,'employee':employee,'title':'{0}-{1} leave'.format(leave.user.username,leave.status)})





