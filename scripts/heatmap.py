import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# ANSI US QWERTY layout
keyboard_rows = [
    ["`","1","2","3","4","5","6","7","8","9","0","-","=","Backspace"],
    ["Tab","q","w","e","r","t","y","u","i","o","p","[","]","\\"],
    ["CapsLock","a","s","d","f","g","h","j","k","l",";","'","Enter"],
    ["Shift","z","x","c","v","b","n","m",",",".","/","Shift"],
    ["Ctrl","Win","Alt","Space","Alt","Fn","Menu","Ctrl"]
]

# Actual approximate key widths in "units" (1 = normal key)
key_widths = {
    "`":1, "1":1, "2":1, "3":1, "4":1, "5":1, "6":1, "7":1, "8":1, "9":1, "0":1, "-":1, "=":1,
    "Backspace":2.25,
    "Tab":1.5, "q":1, "w":1, "e":1, "r":1, "t":1, "y":1, "u":1, "i":1, "o":1, "p":1, "[":1, "]":1, "\\":1.5,
    "CapsLock":1.75, "a":1, "s":1, "d":1, "f":1, "g":1, "h":1, "j":1, "k":1, "l":1, ";":1, "'":1, "Enter":2.25,
    "Shift":2.25, "z":1, "x":1, "c":1, "v":1, "b":1, "n":1, "m":1, ",":1, ".":1, "/":1, 
    "Ctrl":1.25, "Win":1.25, "Alt":1.25, "Space":6.25, "Fn":1.25, "Menu":1.25
}

# Load frequencies from CSV
def load_frequencies(csv_path):
    freqs = {}
    with open(csv_path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            letter = row['letter'].lower()
            try:
                freq = float(row['freq_%'])
            except ValueError:
                continue
            freqs[letter] = freq
    return freqs

# Plot keyboard heatmap
def plot_keyboard_heatmap(freqs):
    # Calculate total width for figure scaling
    total_width = sum(max(key_widths.get(k,1) for k in row) for row in keyboard_rows)
    
    fig, ax = plt.subplots(figsize=(18,6))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 6)
    ax.axis("off")

    max_freq = max(freqs.values()) if freqs else 1.0

    y = 5
    for row in keyboard_rows:
        x = 0
        for key in row:
            w = key_widths.get(key, 1)
            display_key = key.lower()
            freq = freqs.get(display_key, 0)
            intensity = freq / max_freq if max_freq > 0 else 0
            color = (1-intensity, 1-intensity, 1)  # tonalità blu
            rect = patches.Rectangle((x, y), w, 1, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)
            # Adjust font size based on key width
            fontsize = 10 if w <= 1 else 8
            ax.text(x + w/2, y + 0.5, key, ha="center", va="center", fontsize=fontsize)
            x += w + 0.05  # small gap between keys
        y -= 1.05  # small vertical gap between rows

    plt.title("Keyboard Heatmap (ANSI US Layout)", fontsize=16)
    plt.tight_layout()
    plt.show()

# Main
if __name__ == "__main__":
    csv_file = "results.csv"
    if not os.path.isfile(csv_file):
        print(f"Errore: il file {csv_file} non esiste.")
    else:
        freqs = load_frequencies(csv_file)
        plot_keyboard_heatmap(freqs)

