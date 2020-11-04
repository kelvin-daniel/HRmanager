from django import forms
from .models import *
#from .models import


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Business