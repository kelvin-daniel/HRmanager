from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    logo = CloudinaryField('image', null=True)
    description = HTMLField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = PhoneNumberField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    avatar = CloudinaryField('image', null=True)
    description = HTMLField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name