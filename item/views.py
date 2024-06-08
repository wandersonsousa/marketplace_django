from django.shortcuts import render, get_object_or_404
from .models import Item


def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, "item/detail.html", {"item": item})
