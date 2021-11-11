from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
from .somewhere import handle_uploaded_file
# Create your views here.


def EmployeeFormView(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            
             form.save()
             return redirect('employeeData')

    context = {'form':form}
    template_name = 'app1/mediaForm.html'
    return render(request,template_name,context)

def EmployeeData(request):
    obj = Employee.objects.all()
    template_name = 'app1/employeeData.html'
    context = {'data':obj}
    return render(request,template_name,context)

