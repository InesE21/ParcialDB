from django.urls import path
from MyApps.logistics.views import transport_list, transport_detail, service_list, service_detail, route_list, route_detail, routeTransport_list, routeTransport_detail

urlpatterns = [
    path('transport/', transport_list),
    path('transport/<int:pk>/', transport_detail),
    path('service/', service_list),
    path('service/<int:pk>/', service_detail),
    path('route/', route_list),
    path('route/<int:pk>/', route_detail),
    path('routeTransport/', routeTransport_list),
    path('routeTransport/<int:pk>/', routeTransport_detail),
]
