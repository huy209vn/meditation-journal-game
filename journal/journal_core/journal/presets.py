# journal/presets.py
from __future__ import annotations
from typing import Dict, List


class PresetManager:
    """Stores default + custom presets in memory for now."""

    def __init__(self) -> None:
        self._presets: Dict[str, List[str]] = {
            "daily_reflection": [
                "Mood:",
                "What went well today?",
                "What challenged me?",
                "One thing I'm grateful for:",
            ],
            "work_log": [
                "Task completed:",
                "Time taken:",
                "Challenges:",
                "Next steps:",
            ],
        }

    # ---------- CRUD ----------
    def list(self) -> list[str]:
        return list(self._presets.keys())

    def get(self, name: str) -> list[str]:
        return self._presets.get(name, [])

    def add(self, name: str, prompts: list[str]) -> None:
        if name in self._presets:
            raise ValueError(f"Preset '{name}' already exists.")
        self._presets[name] = prompts

    def delete(self, name: str) -> None:
        self._presets.pop(name, None)