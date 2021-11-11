from django.urls import path
from .views import EmployeeData, EmployeeFormView
urlpatterns = [
    path('employee/',EmployeeFormView,name = 'employee'),
    path('employeeData/',EmployeeData,name = 'employeeData'),


]