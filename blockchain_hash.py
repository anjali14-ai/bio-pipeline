# Day 6 — Blockchain Hashing for Bioinformatics Data
# Author: Anjali

import hashlib

# Path to your FASTA file fetched from NCBI
file_path = "fasta-files/COX1_gene.fasta"

# Read the file as binary (recommended for hashing)
with open(file_path, "rb") as f:
    data = f.read()

# Generate SHA-256 hash
data_hash = hashlib.sha256(data).hexdigest()

# Print result
print("🔐 SHA-256 Hash of COX1_gene.fasta:\n", data_hash)

# Save hash into a verification file
with open("fasta-files/data_hash.txt", "w") as h:
    h.write(f"COX1_gene.fasta  {data_hash}\n")

print("\n✅ Hash stored in fasta-files/data_hash.txt")
