from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from MyApps.shipments.models import Correspondence, Shipping, Incident
from MyApps.shipments.serializers import CorrespondenceSerializer, ShippingSerializer, IncidentSerializer

@api_view(['GET', 'POST'])
def correspondence_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        correspondence = Correspondence.objects.all()
        serializer = CorrespondenceSerializer(correspondence, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CorrespondenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def correspondence_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        correspondence = Correspondence.objects.get(pk=pk)
    except Correspondence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CorrespondenceSerializer(correspondence)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CorrespondenceSerializer(correspondence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        correspondence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def shipping_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        shipping = Shipping.objects.all()
        serializer = ShippingSerializer(shipping, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShippingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def shipping_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        shipping = Shipping.objects.get(pk=pk)
    except Shipping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShippingSerializer(shipping)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ShippingSerializer(shipping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        shipping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def incident_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        incident = Incident.objects.all()
        serializer = IncidentSerializer(incident, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def incident_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        incident = Incident.objects.get(pk=pk)
    except Incident.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)