from django.db import models
from MyApps.branches.models import Branch
from MyApps.logistics.models import Route

class Customer(models.Model):
    dni = models.IntegerField(unique = True, verbose_name='dni')
    fullname = models.CharField(max_length=50, verbose_name='fullname')
    address = models.CharField(max_length=50, verbose_name='address')
    phoneNumber = models.CharField(max_length=50, verbose_name='phone number')
    mail = models.EmailField(unique = True, verbose_name='mail')

    CUSTOMER_TYPE_CHOICES = [
        ['NORMAL', 'Normal'],
        ['PREMIUM', 'Premium']
    ]

    customer_type = models.CharField(max_length=7, choices=CUSTOMER_TYPE_CHOICES, help_text="Select Customer Type")

    def _str_(self):
        return self.fullname
    
    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"

class Employee(models.Model):
    fullname = models.CharField(max_length=50, verbose_name='fullname')

    POSITION_EMPLOYEE_CHOICES = [
        ['MANAGER', 'Manager'],
        ['ADVISOR', 'Advisor'],
        ['DISTRIBUTOR', 'Distributor'],
        ['SUPERVISOR', 'Supervisor'],
    ]

    position = models.CharField(max_length=11, choices=POSITION_EMPLOYEE_CHOICES, help_text="Select Position Employee")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='Branch')
    assignedRoute = models.ForeignKey(Route, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Assigned Route')

    def clean(self):
        """Validación para asegurar que 'assigned_route' solo se asigne si la posición es 'DISTRIBUTOR'."""
        from django.core.exceptions import ValidationError

        if self.position == 'DISTRIBUTOR' and not self.assignedRoute:
            raise ValidationError({'assignedRoute': "The assigned route is mandatory for distributors."})
        elif self.position != 'DISTRIBUTOR' and self.assignedRoute:
            raise ValidationError({'assignedRoute': "The route must only be assigned to distributors."})

    def _str_(self):
        return self.fullname

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"

