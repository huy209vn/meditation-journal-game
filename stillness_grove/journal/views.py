"""Placeholder views for the journal app."""

from django.http import HttpResponse


def entry_list(request):
    """Return a simple list of journal entries."""
    return HttpResponse("Journal entry list placeholder")


def entry_create(request):
    """Return a placeholder page for creating a new journal entry."""
    return HttpResponse("Journal entry creation placeholder")
