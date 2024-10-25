from django.contrib import admin
from .models import Transport, Route, RouteTransport, Service

class RouteTransportInline(admin.TabularInline):
    model = RouteTransport
    extra = 1  

class TransportAdmin(admin.ModelAdmin):
    list_display = ('transportation', 'capacity')
    search_fields = ('transportation',)

class RouteAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'stops')
    search_fields = ('origin', 'destination')
    inlines = (RouteTransportInline,)

class RouteTransportAdmin(admin.ModelAdmin):
    list_display = ('route', 'transport')
    list_filter = ('route', 'transport')

class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(RouteTransport, RouteTransportAdmin)