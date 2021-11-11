from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    image = forms.ImageField()
    document = forms.FileField()
    class Meta:
        model = Employee
        fields = '__all__'