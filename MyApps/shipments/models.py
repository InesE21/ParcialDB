from django.db import models
from MyApps.persons.models import Customer, Employee
from MyApps.logistics.models import Service
import random
import string

class Correspondence(models.Model):
    code = models.CharField(max_length=6, verbose_name="correspondence code", unique=True, editable=False)
    correspondenceType = models.CharField(max_length=30, verbose_name="correspondence type")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="weight")
    dimensions = models.CharField(max_length=50, verbose_name="dimensions")
    shipmentDate = models.DateTimeField(verbose_name="shipment date")
    deliveryDate = models.DateTimeField(verbose_name="delivery date")
    sender = models.ForeignKey(Customer, related_name='sent_correspondences', on_delete=models.CASCADE, verbose_name='sender')
    receiver = models.ForeignKey(Customer, related_name='received_correspondences', on_delete=models.CASCADE, verbose_name='receiver')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='service')

    def generate_tracking_code(self):
        characters = string.ascii_uppercase + string.digits 
        return ''.join(random.choices(characters, k=6))

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_tracking_code()
        super().save(*args, **kwargs)

    def _str_(self):
        return self.code
    
    class Meta:
        verbose_name = 'correspondence'
        verbose_name_plural = 'correspondences'

class Shipping(models.Model):

    SHIPPING_STATUS_CHOICES = [
        ['AT ORIGIN', 'At origin'],
        ['AT DESTINATION', 'At destination'],
        ['ON THE WAY', 'On the way'],
        ['DELIVERED', 'Deliveres'],
    ]

    status = models.CharField(max_length=20, choices=SHIPPING_STATUS_CHOICES, verbose_name="shipping status")
    dateTime = models.DateTimeField(verbose_name="date and time")
    correspondence = models.ForeignKey(Correspondence, on_delete=models.CASCADE, verbose_name='correspondence')
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE, verbose_name='branch')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='responsible employee')

    def _str_(self):
        return f'{self.status} - {self.dateTime}'
    
    class Meta:
        verbose_name = 'shipping'
        verbose_name_plural = 'shippings'

class Incident(models.Model):
    description = models.TextField(verbose_name='description')
    incidentDate = models.DateTimeField(verbose_name='incident date')

    RESOLUTION_STATUS_CHOICES = [
        ['REPORTED', 'Reported'],
        ['SCALED', 'Scaled'],
        ['IN RESOLUTION', 'In resolution'],
        ['RESOLVED', 'Resolved'],
        ['CLOSED', 'Closed'],
    ]

    resolutionStatus = models.CharField(max_length=20, choices=RESOLUTION_STATUS_CHOICES, verbose_name="resolution status")
    correspondence = models.ForeignKey(Correspondence, on_delete=models.CASCADE, verbose_name='correspondence')

    def _str_(self):
        return f'{self.description} - {self.resolutionStatus}'