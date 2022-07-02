from django import forms
from .models import Enterprise, Employee, Position

class RegisterEnterprise(forms.ModelForm):

    class Meta:
        model = Enterprise

        fields =[
            'name',
            'email',
            'phone',
            'address_line_1',
            'address_line_2',
            'state',
            'city',
            'country',
            'zipcode',
        ]

    def __init__(self, *args, **kwargs):
        super(RegisterEnterprise, self).__init__(*args, **kwargs)
        self.fields['address_line_2'].required = False
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

class EmployeeRegistration(forms.ModelForm):

    class Meta:
        
        model = Employee

        fields =[
            'full_name',
            'email',
            'phone',
            'ssn',
            'salary', 
            'role',
        ]

    def __init__(self, *args, **kwargs):
        self.request= kwargs.pop('request', None)
        super(EmployeeRegistration, self).__init__(*args, **kwargs)
        param = Enterprise.objects.get(account=self.request.user)
        self.fields['role'].queryset = Position.objects.filter(enterprise=param.id)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

class EmployeeEdit(forms.ModelForm):

    class Meta:

        model = Employee

        fields = [
            'full_name',
            'email',
            'phone',
            'salary',
            'role',
        ]

    def __init__(self, *args, **kwargs):
        self.request= kwargs.pop('request', None)
        super(EmployeeEdit, self).__init__(*args, **kwargs)
        param = Enterprise.objects.get(account=self.request.user)
        self.fields['role'].queryset = Position.objects.filter(enterprise=param.id)
        self.fields['role'].required= False
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'    

class PositionForm(forms.ModelForm):

    class Meta:

        model = Position

        fields = [
            'name',
        ]

    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
