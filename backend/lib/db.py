"""In-memory / persistent store helper for IGNIS investigations."""
from data import ALL_INVESTIGATIONS

_STORE = list(ALL_INVESTIGATIONS)

def init_db(items):
    global _STORE
    _STORE = list(items)

def get_all():
    return _STORE
