from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
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

class Make_user(models.Model):
    avatar = CloudinaryField('image', null=True)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)

    def __str__(self):
        return self.name