"""Simple in-memory journal package."""

from .entry import JournalEntry
from .memory_store import MemoryStorage

__all__ = ["JournalEntry", "MemoryStorage"]
