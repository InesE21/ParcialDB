from django.db import models

# Create your models here.


class Transport(models.Model):
    TRANSPORT_TYPE_CHOICES = [
        ['PLANE', 'Plane'],
        ['TRUCK', 'Truck'],
        ['MOTORBIKE', 'Motorbike'],
    ]

    transportation = models.CharField(max_length=11, choices=TRANSPORT_TYPE_CHOICES, help_text="Select type transport")
    capacity = models.IntegerField(verbose_name="capacity")

    def _str_(self):
        return self.transportation

    class Meta:
        verbose_name = "transport"
        verbose_name_plural = "transports"

class Route(models.Model):
    origin = models.CharField(max_length=50, verbose_name="origin")
    destination = models.CharField(max_length=50, verbose_name="destination")
    stops = models.CharField(max_length=50, verbose_name="stops", blank=True, null=True)
    transport = models.ManyToManyField(Transport, through='RouteTransport', verbose_name='RouteTransport')

    def _str_(self):
        return f'{self.origin} -> {self.destination}'

    class Meta:
        verbose_name = "route"
        verbose_name_plural = "routes"

class Service(models.Model):
    SERVICE_TYPE_CHOICES = [
        ['EXPRESS', 'Express'],
        ['NORMAL', 'Normal'],
    ]

    transportation = models.CharField(max_length=11, choices=SERVICE_TYPE_CHOICES, help_text="Select type transport")
    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="cost")

    def _str_(self):
        return self.transportation

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"

class RouteTransport(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="route")
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, verbose_name="transport")