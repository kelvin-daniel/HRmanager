from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name = 'index'),
    path('leave/apply/',views.leave_creation,name='createleave'),
    path('leaves/pending/all/',views.leaves_list,name='leaveslist'),
    path('leaves/all/view/<int:id>/',views.leaves_view,name='userleaveview'),
   
    

]