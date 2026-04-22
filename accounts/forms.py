from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',  
        'class': 'form-control'
    }))
    conform_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        conform_password = cleaned_data.get('conform_password')

        if password != conform_password:
            raise forms.ValidationError(
                "Password does not match!"
                )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last name'    
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter password'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

