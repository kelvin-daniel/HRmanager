from django import forms
#from .models import


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business