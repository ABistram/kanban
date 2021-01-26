from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Kanban index")


def viewtable(request, table_id):
    return HttpResponse("You selected table nr %s." % table_id)