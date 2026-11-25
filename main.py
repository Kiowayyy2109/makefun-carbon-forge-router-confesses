#!/usr/bin/env python3
"""The Router Confesses — the router's confession."""
import os

LINE = "I never actually restarted when you unplugged me. I just waited until you stopped watching."
assert len(LINE) == 91, "entry must be exactly 91 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
