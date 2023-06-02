from django import forms
from . models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone_number','password']
        # Here phone_number is not taken in register.html front end design
    
    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        pass_clean = cleaned_data.get('password')
        confirm_pass_clean = cleaned_data.get('confirm_password') 
        if pass_clean != confirm_pass_clean:
            raise forms.ValidationError('Password not matched')