from journal.entry import JournalEntry
from journal.memory_store import MemoryStorage

def test_add_and_get():
    store = MemoryStorage()
    e = JournalEntry(text="Hello")
    store.add_entry(e)
    assert store.get_entry(e.id) is e

def test_list_order():
    store = MemoryStorage()
    e1, e2 = JournalEntry(text="One"), JournalEntry(text="Two")
    store.add_entry(e1); store.add_entry(e2)
    ids = [e.id for e in store.list_entries()]
    assert ids == [e1.id, e2.id]