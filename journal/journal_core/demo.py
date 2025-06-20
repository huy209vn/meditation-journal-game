# demo_preset.py
from journal.presets import PresetManager
from journal.entry import JournalEntry

pm = PresetManager()
pm.add("gratitude", ["I'm grateful for:", "Why?"])

filled = "\n".join(f"{q} ..." for q in pm.get("gratitude"))
entry = JournalEntry(text=filled, preset="gratitude")
print(entry)