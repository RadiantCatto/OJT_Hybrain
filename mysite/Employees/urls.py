from django.urls import path
from .views import (
    MainEmployees,
    EmployeeDetails,
    EmployeesRegularization,
    WorkSchedulesView
)

urlpatterns = [
    # List all employees
    path('employees', MainEmployees.as_view(), name='employee-list'),
    # Employees with paginator (employees/?page_number=2&page_size=20)
    path('employees', MainEmployees.as_view(), name='employee-list'),
    #Get the Employees in the Employees/search/?keyword=
    path('employees/search', MainEmployees.as_view(), name='employee-search'),
    # Create a new employee
    path('employees/create/', MainEmployees.as_view(), name='create-employee'),
    # Update AN Employee record partially using PATCH method
    path('employees/<int:pk>/edit/', MainEmployees.as_view(), name='edit_employee'),
    # Delete an employee record using DELETE method
    path('employees/delete/<int:pk>/', MainEmployees.as_view(), name='delete-employee'),
    # uses WorkSchedulesView to handle POST requests for creating/updating work schedules
    # Retrieve,  an employee by id
    path('employees/<int:pk>/', EmployeeDetails.as_view(), name='employee_detail'),
    # Update AN Employee  record partially using PATCH method validates the Regularization
    path('employees/update/<int:pk>/', EmployeesRegularization.as_view(), name='update_employee'),
    path('workschedules/', WorkSchedulesView.as_view())
]
