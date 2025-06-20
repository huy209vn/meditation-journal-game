"""Compatibility wrapper for the old :mod:`journal_core` package.

This module now simply re-exports the public API from :mod:`journal` so that
imports like ``import journal_core`` continue to work."""

from journal import *
