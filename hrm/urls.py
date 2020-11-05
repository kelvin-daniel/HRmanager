from django.urls import path, include, re_path
from . import views

urlpatterns = [
    #url('', views.index, name = 'index'),
    path('api/company/', views.CompanyList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/employee/', views.EmployeeList.as_view()),

]