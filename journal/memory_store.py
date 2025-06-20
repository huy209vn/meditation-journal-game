from __future__ import annotations

from typing import Dict, List, Optional

from .entry import JournalEntry


class MemoryStorage:
    """In-memory storage for :class:`JournalEntry`."""

    def __init__(self) -> None:
        self._entries: Dict[str, JournalEntry] = {}
        self._order: List[str] = []

    # -- basic CRUD ---------------------------------------------------------
    def add_entry(self, entry: JournalEntry) -> None:
        self._entries[entry.id] = entry
        self._order.append(entry.id)

    def get_entry(self, entry_id: str) -> Optional[JournalEntry]:
        return self._entries.get(entry_id)

    def list_entries(self) -> List[JournalEntry]:
        return [self._entries[eid] for eid in self._order]
