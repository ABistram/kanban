from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Tables

# Create your views here.


def index(request):
    all_tables = Tables.objects.all()
    template = loader.get_template('index.html')
    context = {
        'tables': all_tables
    }
    return HttpResponse(template.render(context, request))


def viewtable(request, table_id):
    return HttpResponse("You selected table nr %s." % table_id)