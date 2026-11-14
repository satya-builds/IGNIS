"""Seed script to initialize and validate the 18 PSI flight investigations."""
from data import ALL_INVESTIGATIONS
from lib.db import init_db

if __name__ == "__main__":
    init_db(ALL_INVESTIGATIONS)
    print(f"Seeded {len(ALL_INVESTIGATIONS)} investigations successfully.")
