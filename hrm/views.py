from django.shortcuts import render
from .models import *
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
#from .serializer import
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
