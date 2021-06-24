import markdown2 as mk

from django.shortcuts import render
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "entrytitle": entry.capitalize(),
        "entry": util.get_entry(entry)
    })

def entry_not_found(request):
    return render(request, "encyclopedia/entry_not_found.html")