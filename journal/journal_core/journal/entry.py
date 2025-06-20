

# journal/entry.py
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import uuid


@dataclass
class JournalEntry:
    """
    One journal record.

    Args:
        text:  The full entry text (can include \n).
        preset: Name of the preset used, or None for free-form.
    """
    text: str
    preset: str | None = None
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    # --- Helpers -------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "text": self.text,
            "preset": self.preset,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "JournalEntry":
        return cls(
            text=data["text"],
            preset=data.get("preset"),
            created_at=datetime.fromisoformat(data["created_at"]),
            id=data["id"],
        )

    def __str__(self) -> str:       # pretty print
        preview = (self.text[:30] + "…") if len(self.text) > 30 else self.text
        return f"<Entry {self.id[:8]} | {preview}>"