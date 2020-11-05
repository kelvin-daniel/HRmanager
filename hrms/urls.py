"""hrms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hrm.urls')),
    path('logout/', auth_views.LogoutView.as_view(), {"next_page":'/'}),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
    #---work-on-edit-view------#
    path('bank/edit/<int:id>/',views.employee_bank_account_update,name='accountedit'),
    path('leave/apply/',views.leave_creation,name='createleave'),
    path('leaves/pending/all/',views.leaves_list,name='leaveslist'),
    path('leaves/approved/all/',views.leaves_approved_list,name='approvedleaveslist'),
    path('leaves/cancel/all/',views.cancel_leaves_list,name='canceleaveslist'),
    path('leaves/all/view/<int:id>/',views.leaves_view,name='userleaveview'),
    path('leaves/view/table/',views.view_my_leave_table,name='staffleavetable'),
    path('leave/approve/<int:id>/',views.approve_leave,name='userleaveapprove'),
    path('leave/unapprove/<int:id>/',views.unapprove_leave,name='userleaveunapprove'),
    path('leave/cancel/<int:id>/',views.cancel_leave,name='userleavecancel'),
    path('leave/uncancel/<int:id>/',views.uncancel_leave,name='userleaveuncancel'),
    path('leaves/rejected/all/',views.leave_rejected_list,name='leavesrejected'),
    path('leave/reject/<int:id>/',views.reject_leave,name='reject'),
    path('leave/unreject/<int:id>/',views.unreject_leave,name='unreject'),
]
