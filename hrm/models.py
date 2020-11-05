from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model as user_model
User = user_model()
from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
#from .models import ManagerProfile




class Hradmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
 
class EmployeeProfile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	   

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=1024)
    logo = models.ImageField()
    members = models.ManyToManyField(User, through='members')
    
    def __str__(self):
        return self.team_name



# class TeamManager(models.Manager):
#     use_for_related_fields = True

#     def add_member(self, user, team):
#         pass
        
class TeamManagerProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone_number = models.IntegerField(blank=True, null= True)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to = 'profilepics/', blank=True)
    team_name = models.ForeignKey(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name 


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  
        if instance.is_teamlead:  
            TeamLeadProfile.objects.create(user=instance) 

        else:
            pass
    


class MembersProfile(models.Model):
    team_name = models.ForeignKey(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #employee = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


    objects = TeamManager()