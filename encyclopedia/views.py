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
        "entry": mk.markdown(util.get_entry(entry))
    })

