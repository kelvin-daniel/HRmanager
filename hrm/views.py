from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# from .serializer import
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib import messages
from .serializer import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import status

class TeamManagerProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    def check_role(self, request):
        if request.user.is_supervisor:
            pass
        else:
            raise Http404()       
    
    def get_teammanager(self, pk):
        try:
            return TeamManagerProfile.objects.get(pk=pk)
        except TeamManagerProfile.DoesNotExist:
            raise Http404()
    

    def get(self, request, pk, format=None):
        self.check_role(request)
        this_teammanager = self.get_supervisor(pk)
        serializers = TeamManagerSerializer(this_teammanager)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        self.check_role(request)
        this_supervisor = self.get_supervisor(pk)
        serializers = TeamManagerSerializer(this_teamManager, request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        self.check_role(request)
        this_teammanager = self.get_teammanager(pk)
        this_teammanager.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MembersView(APIView):
    permission_classes = (IsAuthenticated,)
    def check_role(self, request):
        if request.user.is_teammanager:
            pass
        else:
            raise Http404()    

    def get(self, request, format=None):
        self.check_role(request)
        all_members = Member.objects.all()
        serializers = MemberSerializer(all_members, many=True)
        return Response(serializers.data) 

    def post(self, request, format=None):
        self.check_role(request)
        serializers = MemberSerializer(data=request.data, partial=True)
        if serializers.is_valid():
            this_member_id = int(serializers.validated_data['member_id_num'])
            this_member = MemberProfile.objects.get(pk=this_member_id)
            serializers.save(member=this_member)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamView(APIView):
    permission_classes = (IsAuthenticated,)
    def check_role(self, request):
        if request.user.is_teammanager or request.user.is_teammanager:
            pass
        else:
            raise Http404()       
    
    def get_team(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404()
    

    def get(self, request, pk, format=None):
        self.check_role(request)
        this_team = self.get_team(pk)
        serializers = TeamSerializer(this_department)
        return Response(serializers.data)


    def put(self, request, pk, format=None):
        self.check_role(request)
        this_team = self.get_team(pk)
        serializers = TeamSerializer(this_team, request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        self.check_role(request)
        this_team = self.get_team(pk)
        this_team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# def employee_profile_view(request):
	
#   if request.method == 'POST':
		
#     user_form = UserForm(request.POST, prefix='UF')
# 		profile_form = EmployeeProfileForm(request.POST, prefix='PF')
		
#     if user_form.is_valid() and profile_form.is_valid():
# 			user = user_form.save(commit=False)
# 			user.save()

# 			user.employee_profile.name = profile_form.cleaned_data.get('name')
#             user.employee_profile.avatar = profile_form.cleaned_data.get('file')
# 			user.employee_profile.phone = profile_form.cleaned_data.get('phone')
#             user.employee_profile.email = profile_form.cleaned_data.get('email')

# 			user.employee_profile.save()
			
# 	else:
# 		user_form = UserForm(prefix='UF')
# 		profile_form = EmployeeProfileForm(prefix='PF')
		
# 	return render(request, '',{
			
# 		})

# Create your views here.
class CompanyList(APIView):
    def get(self, request, format=None):
        all_companies = Company.objects.all()
        serializers = CompanySerializer(all_companies, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        hr_profiles = Profile.objects.all()
        serializers = ProfileSerializer(hr_profiles, many=True)
        return Response(serializers.data)

class EmployeeList(APIView):
    def get(self, request, format=None):
        all_employees = Employee.objects.all()
        serializers = EmployeeSerializer(all_employees, many=True)
        return Response(serializers.data)

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


@login_required(login_url='/accounts/login/')
def companies(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    companies = Company.objects.all()

    return render(request,'companies.html',{"companies":companies})

@login_required(login_url='/accounts/login/')
def employee(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    employees=Employee.objects.all()

    return render(request,'employee.html',{"employees":employees})


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

