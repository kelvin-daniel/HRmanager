from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns=[
    path('supervisor/<int:pk>/', views.TeamManagerProfileView.as_view()),
    path('members/', views.MembersView.as_view()),
    path('team/<int:pk>/', views.TeamView.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

