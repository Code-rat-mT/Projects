import tkinter as tk
from tkinter import ttk
import random

width = 800
height = 800

# Simulate data
def generate_data():
    data = []
    for i in range(6, 19):
        ts = f"2025-05-15 {i}:00"
        s = round(random.uniform(2, 6), 2)
        c = round(random.uniform(1, 4), 2)
        imp = max(0, c - s)
        exp = max(0, s - c)
        credit = round(exp * 1.5, 2)
        data.append((ts, s, c, imp, exp, f"ZMW {credit}"))
    return data

# Main window
def create():
    
    root = tk.Tk()
    root.title("Solar Net-Metering Dashboard")

    # Center the window on screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))
    root.geometry(f"{width}x{height}+{x}+{y}")

    # ---------- Metrics Frame ----------
    metrics_frame = tk.Frame(root)
    metrics_frame.pack(pady=10)

    def create_metric_card(parent, title, value, unit):
        card = tk.Frame(parent, bg="white", bd=1, relief="solid", padx=20, pady=10)
        card.pack(side="left", padx=10)
        tk.Label(card, text=title, font=("Helvetica", 12, "bold")).pack()
        tk.Label(card, text=f"{value} {unit}", font=("Helvetica", 16), fg="green").pack()

    create_metric_card(metrics_frame, "Solar Generated", "42.3", "kWh")
    create_metric_card(metrics_frame, "Grid Consumption", "15.7", "kWh")
    create_metric_card(metrics_frame, "Exported to Grid", "26.1", "kWh")
    create_metric_card(metrics_frame, "Net Credit", "+ZMW 39.15", "")

    # ---------- Table Frame ----------
    table_frame = tk.Frame(root)
    table_frame.pack(pady=10, fill="x")

    columns = ("Timestamp", "Solar (kWh)", "Consumed (kWh)", "Imported (kWh)", "Exported (kWh)", "Credit")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=130, anchor="center")
    tree.pack(fill="x")

    # Scrollbar
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Insert generated data
    for row in generate_data():
        tree.insert("", "end", values=row)

    # ---------- Tariff Info Frame ----------
    tariff_frame = tk.Frame(root)
    tariff_frame.pack(pady=10)

    tk.Label(tariff_frame, text="ZESCO Tariff Info", font=("Helvetica", 12, "bold")).pack()
    tk.Label(tariff_frame, text="Export Rate: ZMW 1.50/kWh | Import Rate: ZMW 2.10/kWh").pack()

    # ---------- System Status Frame ----------
    status_frame = tk.Frame(root)
    status_frame.pack(pady=10)

    tk.Label(status_frame, text="System Status: Online", fg="green", font=("Helvetica", 10)).pack()
    tk.Label(status_frame, text="Inverter: Normal | Battery SOC: 85%", fg="blue", font=("Helvetica", 10)).pack()

    # Run the app
    root.mainloop()

def window():
    create()

