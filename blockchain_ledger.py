import hashlib
import json
import os
from datetime import datetime

LEDGER_FILE = "ledger.json"

# -----------------------------
# 1) Create SHA-256 hash of file
# -----------------------------
def get_file_hash(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

# -----------------------------------------
# 2) Load existing blockchain or start fresh
# -----------------------------------------
def load_ledger():
    if not os.path.exists(LEDGER_FILE):
        return []
    with open(LEDGER_FILE, "r") as f:
        return json.load(f)

# -----------------------------
# 3) Save blockchain to a file
# -----------------------------
def save_ledger(ledger):
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=4)

# -----------------------------
# 4) Add a new block to ledger
# -----------------------------
def add_block(filename, file_hash):
    ledger = load_ledger()
    
    # previous block hash (or 0 for first block)
    prev_hash = ledger[-1]["hash"] if ledger else "0"

    block = {
        "index": len(ledger) + 1,
        "filename": filename,
        "hash": file_hash,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "prev_hash": prev_hash
    }

    ledger.append(block)
    save_ledger(ledger)

    print("\n🧱 New Block Added:\n")
    print(json.dumps(block, indent=4))
    print("\n✅ Blockchain Ledger Updated.")

# -----------------------------
# MAIN EXECUTION
# -----------------------------
FILE_PATH = "fasta-files/COX1_gene.fasta"
file_hash = get_file_hash(FILE_PATH)
add_block(FILE_PATH, file_hash)
