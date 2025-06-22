"""URL configuration for journal views."""

from django.urls import path

from . import views


urlpatterns = [
    path("entries/", views.entry_list, name="entry_list"),
    path("entries/new/", views.entry_create, name="entry_create"),
]
