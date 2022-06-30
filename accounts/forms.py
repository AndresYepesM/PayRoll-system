from django import forms
from django.forms import BaseFormSet
from .models import Account

class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter the password',
        'class':'form-control',
    }))

    confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm the password',
        'class':'form-control',
    }))

    class Meta:

        model = Account

        fields={
            'first_name',
            'last_name',
            'email',
            'phone',
        }
    
    def __init__(self, *args, **kwargs):
        super(UserRegistration, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='First name'
        self.fields['last_name'].widget.attrs['placeholder']='last name'
        self.fields['email'].widget.attrs['placeholder']='email'
        self.fields['phone'].widget.attrs['placeholder']='phone'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

    def clean(self):
        cleaned_data = super(UserRegistration, self).clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('confirm')
        upper = 0

        if password == confirm:
            if len(password) >= 8:
                for i in password:
                    if i.isupper():
                        upper += 1
                
                if upper >= 1:
                    pass

                else:
                    raise forms.ValidationError('The Password need at least one character uppercase')
            else:
                raise forms.ValidationError('The Password need at least 8 characters')
        else:
            raise forms.ValidationError('The password not match please Try Again')
