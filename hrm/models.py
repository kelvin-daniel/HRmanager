from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_hradmin = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

class EmployeeProfile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class TeamLeadProfile(models.Model):
  	user = models.ManyToManyField(User, on_delete=models.CASCADE, null=True, related_name='hr_profile')
	team_name = models.CharField(max_length=100, blank=True)
	website = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        return self.name

    
 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_employee:
		EmployeeProfile.objects.get_or_create(user = instance)
	else:
		TeamLeadProfile.objects.get_or_create(user = instance)
	
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	# print(instance.employeeprofile)
	if instance.is_employee:
		instance.employee_profile.save()
	else:
		TeamLeadProfile.objects.get_or_create(user = instance)
