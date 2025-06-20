"""Compatibility wrapper for the legacy :mod:`journal_core` package.

The original project exposed a package called ``journal_core`` which has since
been renamed simply to :mod:`journal`.  To preserve backwards compatibility,
this lightweight module re-exports the public API from :mod:`journal`.
"""

from importlib import import_module

_j = import_module("journal")

JournalEntry = _j.JournalEntry
MemoryStorage = _j.MemoryStorage

__all__ = list(_j.__all__)
