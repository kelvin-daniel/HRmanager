from django import forms
from .models import Leave
# from .models import Comment
import datetime

class LeaveCreationForm(forms.ModelsForm):
    	reason = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
        class meta:
            model = Leave
            exclude = ['user','defaultdays','hrcomments','status','is_approved','updated','created']


        def clean_enddate(self):
            enddate = self.cleaned_data['enddate']
            startdate = self.cleaned_data['startdate']
            today_date = datetime.date.today()

            if (startdate or enddate) < today_date:
                raise forms.ValidationError("Selected dates are incorrect,please select again")
            elif startdate >= enddate:
                raise forms.ValidationError("Selected dates are wrong")

            return enddate




#class ProfileForm(forms.ModelForm):
    #class Meta:
        #model=Profile

#class CompanyForm(forms.ModelForm):
    #class Meta:
        #model=Company

#class Make_userForm(forms.ModelForm):
    #class Meta:
        #model=Make_user
'''        