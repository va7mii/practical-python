import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

base_path = '/'

def create_page(fig_name, panels, title=""):
    fig, ax = plt.subplots(figsize=(6.625, 10.25), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 155)
    ax.set_aspect('equal')
    ax.axis('off')
    for (x, y, w, h, label) in panels:
        ax.add_patch(Rectangle((x, y), w, h, linewidth=2, edgecolor='black', facecolor='none'))
        ax.text(x + w/2, y + h/2, label, ha='center', va='center', fontsize=6)
    if title:
        ax.text(50, 152, title, ha='center', va='center', fontsize=8, style='italic')
    fpath = os.path.join(base_path, fig_name)
    plt.savefig(fpath, bbox_inches='tight')
    plt.close(fig)
    return fpath

# Define pages
templates = []

# Page 1
templates.append(create_page(
    "manga_template_page1_splash.png",
    [(2, 2, 96, 146, "PANEL 1\nFull Splash")],
    "PAGE 1 – Full Splash"
))

# Page 2
templates.append(create_page(
    "manga_template_page2_action.png",
    [
        (2, 99, 96, 49, "PANEL 1A\nHorizontal"),
        (2, 49, 96, 49, "PANEL 1B\nHorizontal"),
        (2, 2, 31, 45, "PANEL 2A"),
        (35, 2, 31, 45, "PANEL 2B"),
        (68, 2, 30, 45, "PANEL 2C")
    ],
    "PAGE 2 – 2 Horizontal / 3 Vertical"
))

# Page 3
templates.append(create_page(
    "manga_template_page3_mixed.png",
    [
        (2, 103, 96, 45, "PANEL 1\nWide"),
        (2, 52, 45, 47, "PANEL 2A"),
        (2, 2, 45, 47, "PANEL 2B"),
        (49, 2, 49, 97, "PANEL 2C\nTall")
    ],
    "PAGE 3 – Mixed Tall/Stack"
))

# Page 4
templates.append(create_page(
    "manga_template_page4_magic.png",
    [
        (2, 123, 96, 25, "RIBBON SFX"),
        (2, 62, 96, 58, "PANEL 2\nPanoramic"),
        (2, 2, 46, 55, "PANEL 3A"),
        (52, 2, 46, 55, "PANEL 3B")
    ],
    "PAGE 4 – Ribbon & Panoramic"
))

