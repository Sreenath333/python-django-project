from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Items

# Create your views here.

def index(response, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.items_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><br><p>%s</p>" %(ls.name, str(item.text)))

