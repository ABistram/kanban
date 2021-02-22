from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ItemSerializer, FieldSerializer, SheetSerializer, StyleSerializer
from .models import Item, Field, Sheet, Style

# Functions


def get_objects_styles(objects):
    style_dict = {}
    for o in objects:
        style = o.style
        style_dict[o.name] = {
            'height': style.height,
            'width': style.width,
            'background-color': style.bgcolor,
            'color': style.txtcolor,
            'font-size': style.fontsize,
            'border': style.border
        }

    return style_dict


def get_layout_from_fields(fields, parent=None):
    layout = []
    ret_layout = {}
    with_parent = {}
    layout_str = ""

    for f in fields:
        if f.parent is None or f.parent.name == parent:
            pointer = [f.positionX - 1, f.positionY - 1]
            for y in range(f.rowspan):
                while len(layout) - 1 < pointer[1]:
                    layout.append([])
                for x in range(f.colspan):
                    while len(layout[pointer[1]]) - 1 < pointer[0]:
                        layout[pointer[1]].append("Default")
                    layout[pointer[1]][pointer[0]] = f.name
                    pointer[0] += 1
                pointer[1] += 1
                pointer[0] = f.positionX - 1
        else:
            if f.parent not in with_parent:
                with_parent[f.parent] = []
            with_parent[f.parent].append(f)

    for r in layout:
        layout_str += '\"'
        for i in r:
            layout_str += "%s " % i
        layout_str += '\"\n'

    if parent is None:
        ret_layout['container'] = layout_str
    else:
        ret_layout[parent] = layout_str

    for k, f in with_parent.items():
        ret_layout |= get_layout_from_fields(f, k.name)

    return ret_layout

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


@api_view(['GET'])
def kanban_structure(request, table_id):
    sheet = Sheet.objects.get(pk=table_id)
    fields = [Field.objects.filter(sheet=table_id).order_by('positionY', 'positionX')]
    items = Item.objects.none()
    for f in fields[0]:
        i = Item.objects.filter(field=f.id)
        items.union(i)

    structure = {
        'kanban_name': sheet.title,
        'structure': get_layout_from_fields(fields[0]),
        'styles': get_objects_styles((fields[0] | items))
    }

    return Response(structure)
