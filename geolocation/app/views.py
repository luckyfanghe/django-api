from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from geolocation.app.serializers import UserSerializer, GroupSerializer, GeoLocationSerializer
from .models import GeoLocation
import requests

STATUS_APPROVED = 0
STATUS_DENIED = 1
STATUS_PENDING = 2

def querySet_to_list(qs):
    """
    this will return python list<dict>
    """
    return [dict(q) for q in qs]

def index(request):
    return render(request, "index.html")

def pendinglocations(request):
    locations = GeoLocation.objects.filter(status=STATUS_PENDING).values()
    return render(request, "pendinglocations.html", {'locations': list(locations)})

@api_view(['POST'])
def save_user_geolocation(request):
    data = request.POST.dict()
    if GeoLocation.objects.filter(username=data['username']):
        return Response(status=status.HTTP_200_OK, data={'success': False, 'error': 'Already exist! input other username'})

    res = requests.get(f'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={data["latitude"]}&lon={data["longitude"]}').json()
    data['address'] = res['display_name']
    data['status'] = STATUS_PENDING
    serializer = GeoLocationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK, data={'success': True})

    return Response(status=status.HTTP_200_OK, data={'success': False})

@api_view(['POST'])
def change_status(request):
    try:
        geoloc = GeoLocation.objects.get(pk=request.POST['id'])
    except GeoLocation.DoesNotExist:
        return Response(status=status.HTTP_200_OK, data={'success': False})

    if request.POST['status'] == 'approved':
        geoloc.status = STATUS_APPROVED
        geoloc.save()
        return Response(status=status.HTTP_200_OK, data={'success': True})

    if request.POST['status'] == 'denied':
        geoloc.status = STATUS_DENIED
        geoloc.save()
        return Response(status=status.HTTP_200_OK, data={'success': True})

    return Response(status=status.HTTP_200_OK, data={'success': False})