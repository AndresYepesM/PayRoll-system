from django import forms
from .models import Enterprise

class RegisterEnterprise(forms.ModelForm):

    class Meta:
        model = Enterprise

        fields ={
            'name',
            'email',
            'phone',
            'address_line_1',
            'address_line_2',
            'state',
            'city',
            'country',
            'zipcode',
        }

    def __init__(self, *args, **kwargs):
        super(RegisterEnterprise, self).__init__(*args, **kwargs)
        self.fields['address_line_2'].required = False
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'