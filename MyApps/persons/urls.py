from django.urls import path
from MyApps.persons.views import CustomerList, CustomerDetail, EmployeeList, EmployeeDetail


urlpatterns = [
    path('', CustomerList.as_view()),
    path('<int:pk>', CustomerDetail.as_view()),
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>', EmployeeDetail.as_view()),
]