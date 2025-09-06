# QWAK: A Custom Italian Keyboard Layout

## Introduction
QWAK is a custom keyboard layout meticulously designed for the Italian language. Unlike traditional layouts, which were constrained by the mechanical limitations of typewriters, QWAK is built with modern typing needs in mind. Its design is guided by statistical analysis of Italian texts and ergonomic principles, with the goal of maximizing typing efficiency while minimizing finger strain and fatigue.

Most conventional layouts, including QWERTY and ANSI US, reflect compromises made for typewriters. Keys were spread out to prevent jams, and letters were positioned to satisfy mechanical feasibility rather than typing logic. As a result, high-frequency letters could be placed in inconvenient locations, forcing unnecessary finger travel and repeated use of weaker fingers. QWAK discards these historical constraints, leveraging contemporary analysis methods and ergonomic insights to produce a layout optimized for the Italian language.

---

## Motivation
The motivation for QWAK comes from the observation that Italian text exhibits a distinct letter frequency distribution that is poorly served by traditional layouts. Letters like **E, A, I, O, U, S, N, R, T** appear frequently in Italian, but in standard layouts, they are often scattered, forcing long stretches, repeated same-finger usage, and inefficient hand alternation.

Beyond frequency, typing comfort is often neglected in conventional layouts. Lateral finger motion, uneven load distribution, and awkward sequences contribute to fatigue and reduce typing speed. QWAK addresses these issues by strategically placing letters according to frequency, clustering high-use keys centrally, and designing finger motion to be as natural and ergonomic as possible. The result is a layout that feels intuitive, reduces strain, and supports rapid, sustained typing.

---

## Data Collection and Analysis
To inform QWAK's design, a diverse corpus of Italian texts was analyzed. The corpus included dictionaries, historical novels, scientific papers, and stories spanning different styles and vocabulary ranges. This diversity ensures the layout remains effective across multiple writing contexts.

A Python script was used to process each PDF in the corpus. The workflow was as follows:

1. **Text Extraction** – Each page was read and concatenated into a single string.  
2. **Normalization** – Text was converted to lowercase, and all non-letter characters were removed. Accented characters were also excluded at this stage, as they are accessed via a dedicated modifier key.  
3. **Frequency Analysis** – Absolute and relative frequencies of each letter were computed.  
4. **Bigram Analysis** – For each letter, the most common preceding and succeeding letters were recorded to capture common sequences and hand alternation opportunities.  
5. **CSV Export** – Results were saved to a CSV file containing counts, frequencies, and neighboring letters for further analysis.  
6. **Space Density Visualization** – Text was divided into fixed-size blocks, and the proportion of spaces was calculated per block to visualize rhythm and spacing patterns.

The analysis highlighted critical insights:

- Vowels dominate the text in frequency and should be placed strategically.  
- Certain consonants appear in predictable sequences, suggesting optimal hand placement to reduce same-hand repetitions.  
- Clustering high-frequency letters reduces finger travel and improves typing flow.  

This statistical foundation guided every design decision in QWAK, from letter clustering to finger assignment.

---

## Layout Design Principles
### Split Layout
QWAK employs a split keyboard design, which allows for better ergonomics and natural hand alternation. Keys are distributed so that common Italian bigrams often fall on opposite hands, minimizing finger congestion and facilitating smooth typing.

### Vowel Placement
Vowels, being highly frequent, were treated as a special category. Three vowels are placed on one hand and two on the other to encourage alternation between vowels and consonants. This arrangement ensures common Italian words can be typed fluidly, with minimal same-finger repetitions. The exact placement was informed by statistical bigram analysis to balance workload and improve typing flow.

### Centralization of Frequently Used Letters
High-frequency letters such as **E, A, I, O, U, S, N, R, T** are clustered along the central row, placing them under the strongest and most agile fingers. Less frequent letters occupy peripheral positions. Some medium-frequency letters were intentionally compromised to maintain overall hand balance and preserve central clustering. These compromises were informed by the analysis of letter sequences and ergonomic considerations.

---

## Ergonomics Considerations
Human fingers vary in length, strength, and dexterity. QWAK incorporates these differences into its design:

- **Vertical Staggering** – Each column is slightly offset vertically to match natural finger motion, reducing lateral strain.  
- **Longitudinal Finger Motion** – Fingers (except the thumb) primarily move along their natural length rather than sideways, which is more comfortable.  
- **Thumb Design** – The thumb is optimized for horizontal motion and handles the spacebar and lateral keys.  
- **Finger Load Balancing** – Frequent letters are assigned to strong fingers, and workload is distributed evenly across both hands.  

By aligning key placement with natural motion, QWAK minimizes strain, making long typing sessions less fatiguing.

### Accents and Special Characters
Italian accented characters (**à, è, é, ì, ò, ó, ù**) are not placed directly on the main layout. Instead, a dedicated button in the bottom-right corner grants access to accented letters. Modifiers like Shift or Ctrl allow selection of different accents. This approach preserves central typing space for high-frequency letters and maintains the layout's compact, efficient design.

---

## Layout Visualization
### Heatmaps
Heatmaps provide a visual comparison between ANSI US and QWAK layouts.

- **ANSI US Layout**  
  `![Heatmap ANSI](images/US_ANSI_heatmap.png)`  
  Frequent Italian letters are scattered, leading to long stretches, repeated same-finger sequences, and inefficient hand alternation. This reflects the typewriter-influenced design rather than linguistic optimization.

- **QWAK Layout**  
  `![Heatmap QWAK](images/QWAK_heatmap.png)`  
  Letters are clustered according to frequency and bigram patterns, reducing finger travel, increasing hand alternation, and centralizing high-use letters.

### ASCII Render of QWAK
┌─────┬─────┬─────┬─────┬─────┐ ┌─────┬─────┬─────┬─────┬─────┐
│ 1   │  2  │  3  │  4  │  5  │ │  6  │  7  │  8  │  9  │  0  │
├─────┴─────┴─────┴─────┴─────┤ ├─────┴─────┴─────┴─────┴─────┤
│  Q  │  W  │  A  │  K  │space│ │space│  R  │  T  │  H  │  J  │
├─────┴─────┴─────┴─────┤             ├─────┴─────┴─────├─────┴
│  X  │  S  │  E  │  I  │             │  O  │  U  │  N  │  L  │
├─────┴─────┴─────┴─────┤             ├─────┴─────┴─────┤
│ Z   │  C  │  V  │enter      │ │enter      │  M  │  P  │



### Render Placeholders
- Letters Only: `![Letters Only](images/letter_placement_render.png)`  
- Full Keyboard Render: `![Full Render](path/to/render_full.png)`  

---

## Comparison with ANSI Layout
ANSI US keyboards, designed for typewriters, scatter frequent Italian letters and require long stretches and awkward finger movements. QWAK addresses these issues:

- **Finger Travel** – Reduced through clustering of high-frequency letters.  
- **Hand Alternation** – Improved by distributing common bigrams across hands.  
- **Central Row Usage** – Maximized for strongest fingers.  
- **Ergonomic Strain** – Minimized with vertical staggering and motion-aligned keys.

QWAK demonstrates that abandoning historical typewriter constraints allows for a layout tailored to linguistic patterns and human ergonomics.

---

## Conclusion
QWAK shows that keyboards can be designed for actual typing efficiency rather than mechanical constraints. By combining statistical analysis of Italian text with ergonomic principles, QWAK improves typing speed, comfort, and hand alternation while reducing strain.

Future directions include user testing, refinement of vertical offsets, and potential adaptation to other languages. QWAK represents a step toward keyboards that truly serve the way people type today, not the needs of century-old typewriters.

