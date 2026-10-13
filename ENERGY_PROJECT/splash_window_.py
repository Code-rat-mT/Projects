import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import energy_audit as sp
import metering as met
import efficiency as eff
import visualization as vis

def energy():
    sp.window()

def efficiency():
    eff.window()

def metering():
    met.window()

def visualization():
    vis.window()

def main_window():
    splash_root.destroy()
    root = tk.Tk()
    root.title("Energy Audit System")
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.resizable(False, False)
    root.configure(bg="#f0f4f7")

    # Sidebar
    sidebar = tk.Frame(root, width=200, height=height, bg="#2C3E50")
    sidebar.pack(side="left", fill="y")

    tk.Label(sidebar, text="MENU", font=("Arial", 18, "bold"), fg="white", bg="#2C3E50").pack(pady=(30, 20))

    button_style = {
        "font": ("Arial", 12),
        "bg": "#34495E",
        "fg": "white",
        "activebackground": "#1ABC9C",
        "activeforeground": "white",
        "relief": "flat",
        "bd": 0,
        "width": 20,
        "height": 2
    }

    tk.Button(sidebar, text="Energy Audit", command=energy, **button_style).pack(pady=5)
    tk.Button(sidebar, text="Efficiency Measures", command=efficiency, **button_style).pack(pady=5)
    tk.Button(sidebar, text="Net Metering", command=metering, **button_style).pack(pady=5)
    tk.Button(sidebar, text="Visualization", command=visualization, **button_style).pack(pady=5)
    tk.Button(sidebar, text="Exit", command=root.destroy, **button_style).pack(pady=(60, 5))

    # Content Area
    content = tk.Frame(root, bg="#f0f4f7", width=600, height=height)
    content.pack(side="right", fill="both", expand=True)

    tk.Label(content, text="Welcome to the Energy Audit Dashboard",
             font=("Arial", 20, "bold"), bg="#f0f4f7", fg="#2C3E50").pack(pady=(150, 10))

    tk.Label(content, text="Use the menu on the left to navigate the system.",
             font=("Arial", 14), bg="#f0f4f7", fg="#7F8C8D").pack()

    root.mainloop()

# ---------- Splash Screen ----------
splash_root = tk.Tk()
splash_root.title("Splash Screen")
splash_root['bg'] = "#13570D"
splash_root.overrideredirect(True)

width = 800
height = 800
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
splash_root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

TEXT_COLOR1 = "#ffffff"

try:
    image1 = Image.open("ENERGY_PROJECT/pictures/house_energy.png").resize((500, 300))
    eiz_logo = Image.open("ENERGY_PROJECT/pictures/EIZ.png").resize((150, 100))

    photo = ImageTk.PhotoImage(image1)
    eiz_photo = ImageTk.PhotoImage(eiz_logo)

    label1 = tk.Label(splash_root, image=photo, bg="#13570D")
    label1.pack(pady=20)

    tk.Label(splash_root, text="ENERGY AUDIT PROJECT", fg=TEXT_COLOR1, font=("Helvetica", 25, "bold"), bg="#13570D").pack()
    tk.Label(splash_root, image=eiz_photo, bg="#13570D").pack(pady=10)
    tk.Label(splash_root, text="Starting...", fg=TEXT_COLOR1, font=("Helvetica", 20, "italic"), bg="#13570D").pack(pady=20)

    splash_root.photo = photo
    splash_root.eiz_photo = eiz_photo

except FileNotFoundError:
    tk.Label(splash_root, text="Loading...", font=("Helvetica", 16), bg="#13570D", fg="white").pack(pady=20)

splash_root.after(3000, main_window)
splash_root.mainloop()
