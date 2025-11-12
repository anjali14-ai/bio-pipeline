# Day 5 – Fetching Gene Sequences from NCBI using Biopython Entrez

from Bio import Entrez, SeqIO

# Required by NCBI – always include your email
Entrez.email = "yanjali1728@gmail.com"

# 1️⃣ Search NCBI for COX1 gene in humans
search_term = "COX1[Gene] AND Homo sapiens[Organism]"
handle = Entrez.esearch(db="nucleotide", term=search_term, retmax=3)
record = Entrez.read(handle)
handle.close()

print("🔍 Found sequence IDs:", record["IdList"])

# 2️⃣ Fetch the first record
first_id = record["IdList"][0]
fetch_handle = Entrez.efetch(db="nucleotide", id=first_id, rettype="fasta", retmode="text")
seq_data = fetch_handle.read()
fetch_handle.close()

# 3️⃣ Save sequence in your results folder
with open("fasta-files/COX1_gene.fasta", "w") as f:
    f.write(seq_data)

print("✅ Sequence saved as fasta-files/COX1_gene.fasta")

# 4️⃣ Parse and show sequence info
for rec in SeqIO.parse("fasta-files/COX1_gene.fasta", "fasta"):
    print("\n🧬 ID:", rec.id)
    print("Length:", len(rec.seq))
    print("Sequence (first 60 bp):", rec.seq[:60])





