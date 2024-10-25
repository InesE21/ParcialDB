from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from MyApps.logistics.models import Transport, Route, Service, RouteTransport
from MyApps.logistics.serializers import TransportSerializer, RouteSerializer, ServiceSerializer, RouteTransportSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def transport_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        transports = Transport.objects.all()
        serializer = TransportSerializer(transports, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def transport_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        transports = Transport.objects.get(pk=pk)
    except Transport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransportSerializer(transports)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TransportSerializer(transports, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transports.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def route_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def route_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        routes = Route.objects.get(pk=pk)
    except Route.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RouteSerializer(routes)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RouteSerializer(routes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        routes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def service_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def service_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        services = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(services)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServiceSerializer(services, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        services.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def routeTransport_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        routeTransports = RouteTransport.objects.all()
        serializer = RouteTransportSerializer(routeTransports, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RouteTransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def routeTransport_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        routeTransports = RouteTransport.objects.get(pk=pk)
    except RouteTransport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransportSerializer(routeTransports)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RouteTransportSerializer(routeTransports, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        routeTransports.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
