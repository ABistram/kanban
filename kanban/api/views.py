from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ItemSerializer, FieldSerializer, SheetSerializer, StyleSerializer
from .models import Item, Field, Sheet, Style

# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all().order_by('id')
    serializer_class = FieldSerializer


class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all().order_by('id')
    serializer_class = SheetSerializer


class StyleViewSheet(viewsets.ModelViewSet):
    queryset = Style.objects.all().order_by('id')
    serializer_class = StyleSerializer


@api_view(['GET', 'POST'])
def kanban_structure(request):
    structure = {}

    return Response(structure)
