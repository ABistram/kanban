from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ItemSerializer
from .models import Item

# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer
