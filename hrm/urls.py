from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name = 'index'),
    path('leave/apply/',views.leave_creation,name='createleave'),
    path('leaves/pending/all/',views.leaves_list,name='leaveslist'),
    path('leaves/all/view/<int:id>/',views.leaves_view,name='userleaveview'),
    path('api/company/', views.CompanyList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/employee/', views.EmployeeList.as_view()),
    path('supervisor/<int:pk>/', views.TeamManagerProfileView.as_view()),
    path('members/', views.MembersView.as_view()),
    path('team/<int:pk>/', views.TeamView.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


