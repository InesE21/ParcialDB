from django.urls import path
from MyApps.shipments.views import shipping_list, shipping_detail, correspondence_list, correspondence_detail, incident_list, incident_detail

urlpatterns = [
    path('shipping/', shipping_list),
    path('shipping/<int:pk>/', shipping_detail),
    path('correspondence/', correspondence_list),
    path('correspondence/<int:pk>/', correspondence_detail),
    path('incident/', incident_list),
    path('incident/<int:pk>/', incident_detail),
]