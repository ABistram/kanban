from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sheet, Field

# Usable functions.


def generate_kanban(fields):
    layout = []
    fields.order_by('positionY', 'positionX')

    for f in fields:
        pointer = [f.positionX - 1, f.positionY - 1]
        for y in range(f.rowspan):
            if len(layout) - 1 < pointer[1]:
                layout.append([])
            for x in range(f.colspan):
                while len(layout[pointer[1]]) - 1 < pointer[0]:
                    layout[pointer[1]].append("")
                layout[pointer[1]][pointer[0]] = f.name
                pointer[0] += 1
            pointer[1] += 1
            pointer[0] = f.positionX - 1

    kanban = {
        'objects': fields,
        'layout': layout
    }

    return kanban

# Views generators.


def index(request):
    all_tables = Sheet.objects.all()
    template = loader.get_template('index.html')
    context = {
        'tables': all_tables
    }
    return HttpResponse(template.render(context, request))


def view_table(request, table_id):
    """
    Generate a virtual list of fields.
    Then "print" it in html.
    Ex:
    L1-9 - Label field 1-9
    S1-9 - Sticker field 1-9

    {
    objects: [L1, L2, L3, S1, S2, S3],
    layout: [
        [L1, L2, L3],
        [S1, S1, S2],
        [S1, S1, S3]
    ]
    }

    """
    sheet = Sheet.objects.get(pk=table_id)
    fields = Field.objects.filter(sheet=table_id)

    template = loader.get_template('kanban.html')
    context = {
        'sheet': sheet,
        'fields': generate_kanban(fields)
    }

    return HttpResponse(template.render(context, request))
