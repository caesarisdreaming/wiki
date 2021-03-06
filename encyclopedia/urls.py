from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    # path("search", views.search_page, name="search_page")
]