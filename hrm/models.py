from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from phonenumber_field.modelfields import PhoneNumberField
from .manager import LeaveManager
from django.utils.translation import ugettext as _
from django.utils import timezone
from datetime import datetime

# Create your models here.
SICK = 'sick'
CASUAL = 'casual'
EMERGENCY = 'emergency'
STUDY = 'study'

LEAVE_TYPE = (
(SICK,'Sick Leave'),
(CASUAL,'Casual Leave'),
(EMERGENCY,'Emergency Leave'),
(STUDY,'Study Leave'),
)

DAYS = 30

class Leave(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    startdate = models.DateField(verbose_name=_('Start Date'),help_text='leave start date is on ..',null=True,blank=False)
    enddate = models.DateField(verbose_name=_('End Date'),help_text='coming back on ...',null=True,blank=False)
    leavetype = models.CharField(choices=LEAVE_TYPE,max_length=25,default=SICK,null=True,blank=False)
    reason = models.CharField(verbose_name=_('Reason for Leave'),max_length=255,help_text='add additional information for leave',null=True,blank=True)
    defaultdays = models.PositiveIntegerField(verbose_name=_('Leave days per year counter'),default=DAYS,null=True,blank=True)


    status = models.CharField(max_length=12,default='pending')
    is_approved = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = LeaveManager()


    class meta:
        verbose_name = _('Leave')
        verbose_name_plural=_('Leaves')
        ordering = ['-created']

    def __str__(self):
        return ('{0} - {1}'.format(self.leavetype,self.user))


    @property
    def pretty_leave(self):
        leave = self.leavetype
        user = self.user
        employee = user.employee_set.first().get_full_name
        return ('{0} - {1}'.format(employee,leave))

    @property
    def leave_days(self):
        days_count = ''
        startdate = self.startdate
        enddate = self.enddate
        if startdate > enddate:
            return
        dates = (enddate - startdate)
        return dates.days

    @property
    def leave_approved(self):
        return self.is_approved == True

    @property
    def leave_approved(self):
        if not self.is_approved:
            self.is_approved = True
            self.status = 'approved'
            self.save()
    @property
    def leave_approved(self):
        if not self.is_approved:
            self.is_approved=False
            self.is_approved='pending'
            self.save()

    @property
    def leave_approved(self):
        if not self.is_approved or not self.is_approved:
            self.is_approved=False
            self.is_approved='cancelled'
            self.save()
               
    @property
    def leave_approved(self):
        if not self.is_approved or not self.is_approved:
            self.is_approved=False
            self.is_approved='rejected'
            self.save()    

    @property
	def is_rejected(self):
		return self.status == 'rejected'




class Company(models.Model):
    logo = CloudinaryField('image', null=True)
    description = HTMLField()
    name =models.CharField(max_length=100)
    email = models.EmailField()
    location =models.CharField(max_length=100)
    contact = PhoneNumberField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    avatar = CloudinaryField('image', null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    avatar = CloudinaryField('image', null=True)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name