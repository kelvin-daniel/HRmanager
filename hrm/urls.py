from django.urls import path, include, re_path
from . import views

urlpatterns = [
    #url('', views.index, name = 'index'),
    path('api/company/', views.companyList.as_view())
    path('api/company/', views.companyList.as_view())

]