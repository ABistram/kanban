from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sheet

# Create your views here.


def index(request):
    all_tables = Sheet.objects.all()
    template = loader.get_template('index.html')
    context = {
        'tables': all_tables
    }
    return HttpResponse(template.render(context, request))


def viewtable(request, table_id):
    """
    Generate a virtual list of fields.
    Then "print" it in html.
    Ex:
    L1-9 - Label field 1-9
    S1-9 - Sticker field 1-9

    [
        [L1, L2, L3],
        [S1, S1, S2],
        [S1, S1, S3]
    ]

    """
    return HttpResponse("You selected table nr %s." % table_id)