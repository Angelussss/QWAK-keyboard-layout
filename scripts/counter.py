import re
import collections
import csv
import os
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader

def analyze_pdf(pdf_path, output_csv="results.csv", block_size=50000):
    # 1. Leggi PDF
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    # 2. Normalizza testo per lettere
    lowered = text.lower()
    only_letters = re.sub(r"[^a-zàèéìòóù]", "", lowered)

    # 3. Conta lettere
    letter_counts = collections.Counter(only_letters)
    total_letters = sum(letter_counts.values())

    # 4. Conta coppie (bigrammi)
    prev_counts = {ch: collections.Counter() for ch in letter_counts}
    next_counts = {ch: collections.Counter() for ch in letter_counts}

    for i, ch in enumerate(only_letters):
        if i > 0:
            prev_counts[ch][only_letters[i-1]] += 1
        if i < len(only_letters)-1:
            next_counts[ch][only_letters[i+1]] += 1

    # 5. Prepara risultati
    results = []
    for ch, count in letter_counts.most_common():
        freq = count / total_letters * 100
        most_common_prev = prev_counts[ch].most_common(1)
        most_common_next = next_counts[ch].most_common(1)

        prev_letter = most_common_prev[0][0] if most_common_prev else "-"
        next_letter = most_common_next[0][0] if most_common_next else "-"

        results.append({
           # "file": os.path.basename(pdf_path),
            "letter": ch,
            "count": count,
            "freq_%": round(freq, 3),
            "most_common_prev": prev_letter,
            "most_common_next": next_letter
        })

    # 6. Salva su CSV (append se già esiste)
    file_exists = os.path.isfile(output_csv)
    with open(output_csv, "a", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["file", "letter", "count", "freq_%", "most_common_prev", "most_common_next"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for r in results:
            writer.writerow(r)

    print(f"Analisi completata per {pdf_path}. Risultati aggiunti a {output_csv}")

    # 7. Analisi spazi lungo il testo (per rappresentazione 2D)
    space_frequencies = []
    chunks = [lowered[i:i+block_size] for i in range(0, len(lowered), block_size)]

    for chunk in chunks:
        total_chars = len(chunk)
        if total_chars == 0:
            continue
        spaces = chunk.count(" ")
        space_freq = spaces / total_chars
        space_frequencies.append(space_freq)

    # 8. Grafico densità spazi
    plt.figure(figsize=(10,5))
    plt.plot(range(len(space_frequencies)), space_frequencies, marker="o", linestyle="-")
    plt.title(f"Densità di spazi lungo {os.path.basename(pdf_path)}")
    plt.xlabel(f"Blocchi di {block_size} caratteri consecutivi")
    plt.ylabel("Frazione di spazi")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    pdf_path = "text/ _path_ .pdf"   # Sostituisci _path_ con il file PDF che vuoi analizzare
    analyze_pdf(pdf_path)

