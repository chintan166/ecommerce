from django import forms
from .models import Accounts

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirm password'
    }))
    class Meta:
        model = Accounts
        fields = ['first_name','last_name','phone_number','email','password']
        
    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError("password does not match!")
        
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = "enter first name"
        self.fields['last_name'].widget.attrs['placeholder'] = "enter last name"
        self.fields['email'].widget.attrs['placeholder'] = "enter email"
        self.fields['phone_number'].widget.attrs['placeholder'] = "enter phone number"
        self.fields['password'].widget.attrs['placeholder'] = "enter password"
        self.fields['confirm_password'].widget.attrs['placeholder'] = "enter confirm password"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
            
    
        