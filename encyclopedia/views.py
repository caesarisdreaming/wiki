import markdown2 as mk

from django.shortcuts import redirect, render
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.http import urlencode


# def query_process(request):
#     if request.method == "POST":
#         searched = request.POST.get('q', '')
#         entries = util.list_entries()
#         for e in entries:
#             if e.lower() == searched:
#                 print("lol")
#                 search_page(request, searched)

def index(request):
    # query_process(request)
    if request.method == "GET":
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def entry(request, entry):
    # query_process(request)
    if request.method == "GET":
        return render(request, "encyclopedia/entry.html", {
            "entrytitle": entry.capitalize(),
            "entry": mk.markdown(util.get_entry(entry))
        })

def handler404(request, exception):
    return render(request, "encyclopedia/entry_not_found.html", {
        "entry": request.path.replace("/", "")
    })

# def search_page(request, query):
#     return render(request, "encyclopedia/result_page.html", {
#         "query": query
#     })

# def search_page(request):
#     print('ok')
#     if request.method == "GET":
#         searched = request.POST('q')
#         return render(request, "encyclopedia/result_page.html", {
#             'searched': searched
#         })
#     else:
#         return render(request, "encyclopedia/result_page.html", {
#             'searched': searched
#         })

