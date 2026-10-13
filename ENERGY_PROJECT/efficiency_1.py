import tkinter as tk
from tkinter import ttk, messagebox
from openpyxl import Workbook, load_workbook
import os
import random

width = 800
height = 800

# ---------------- Energy Audit Form ------------------
def create_energy_audit_form(parent_canvas):
    def initialize_excel(file_name):
        if not os.path.exists(file_name):
            wb = Workbook()
            ws = wb.active
            ws.title = "Lighting Data"
            ws.append(["Room Name", "Lamps", "Bulb Rating", "Ballast Per Tube", "Lux (Lumens)", "Hours Per Day"])
            wb.save(file_name)

    def update_display(file_name):
        if not os.path.exists(file_name):
            display_label.config(text="No data yet.")
            return
        try:
            wb = load_workbook(file_name)
            ws = wb.active
            rows = list(ws.iter_rows(values_only=True))
            display_text = "\n".join(["   |   ".join(map(str, row)) for row in rows])
            display_label.config(text=display_text)
        except Exception as e:
            display_label.config(text=f"Error reading file: {e}")

    def submit():
        file_name = filename_entry.get().strip()
        if not file_name.endswith(".xlsx"):
            file_name += ".xlsx"

        initialize_excel(file_name)

        data = [
            room_name.get(),
            lamps_entry.get(),
            bulb_rating_entry.get(),
            ballast_entry.get(),
            lux_entry.get(),
            hours_entry.get()
        ]

        try:
            wb = load_workbook(file_name)
            ws = wb.active
            ws.append(data)
            wb.save(file_name)
            messagebox.showinfo("Success", f"Data saved to {file_name}")
            clear_fields()
            update_display(file_name)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save data: {e}")

    def clear_fields():
        for entry in entries:
            entry.delete(0, tk.END)

    parent_canvas.delete("all")
    frame = tk.Frame(parent_canvas, width=width, height=height)
    canvas_window = parent_canvas.create_window(0, 0, anchor="nw", window=frame)
    parent_canvas.config(scrollregion=parent_canvas.bbox("all"))

    tk.Label(frame, text="Excel File Name:", font=20).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    filename_entry = tk.Entry(frame, width=30, font=20)
    filename_entry.insert(0, "lighting_data.xlsx")
    filename_entry.grid(row=0, column=1, padx=10, pady=5)

    labels = ["Room Name", "Lamps", "Bulb Rating", "Ballast Per Tube", "Lux (Lumens)", "Hours Per Day"]
    entries = []

    for i, label_text in enumerate(labels):
        label = tk.Label(frame, text=label_text, font=15)
        label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

        entry = tk.Entry(frame, width=30, font=20)
        entry.grid(row=i+1, column=1, padx=10, pady=5)
        entries.append(entry)

    room_name, lamps_entry, bulb_rating_entry, ballast_entry, lux_entry, hours_entry = entries

    submit_button = tk.Button(frame, text="Submit", font=30, command=submit)
    submit_button.grid(row=len(labels)+1, column=0, columnspan=2, pady=15)

    display_label = tk.Label(frame, text="Excel contents will appear here.", justify="left", anchor="w", font=8)
    display_label.grid(row=len(labels)+2, column=0, columnspan=2, padx=10, pady=10, sticky="w")

    update_display("lighting_data.xlsx")

# ---------------- Net Metering Window ------------------
def open_net_metering(parent_canvas):
    parent_canvas.delete("all")

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

    frame = tk.Frame(parent_canvas, width=width, height=height)
    parent_canvas.create_window(0, 0, anchor="nw", window=frame)
    parent_canvas.config(scrollregion=parent_canvas.bbox("all"))

    metrics_frame = tk.Frame(frame)
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

    table_frame = tk.Frame(frame)
    table_frame.pack(pady=10, fill="x")

    columns = ("Timestamp", "Solar (kWh)", "Consumed (kWh)", "Imported (kWh)", "Exported (kWh)", "Credit")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=130, anchor="center")
    tree.pack(fill="x")

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    for row in generate_data():
        tree.insert("", "end", values=row)

    tk.Label(frame, text="ZESCO Tariff Info", font=("Helvetica", 12, "bold")).pack()
    tk.Label(frame, text="Export Rate: ZMW 1.50/kWh | Import Rate: ZMW 2.10/kWh").pack()
    tk.Label(frame, text="System Status: Online", fg="green").pack()
    tk.Label(frame, text="Inverter: Normal | Battery SOC: 85%", fg="blue").pack()

# ---------------- Efficiency Window ------------------
def open_efficiency(parent_canvas):
    parent_canvas.delete("all")
    frame = tk.Frame(parent_canvas, width=width, height=height, bg="#f7f9fa")
    parent_canvas.create_window(0, 0, anchor="nw", window=frame)
    parent_canvas.config(scrollregion=parent_canvas.bbox("all"))

    BASE_USAGE = {"Lighting": 1200, "HVAC": 3500, "Insulation": 1800}
    SAVINGS = {"Lighting": 0.4, "HVAC": 0.25, "Insulation": 0.3}

    def calculate_savings():
        upgrades = {
            "Lighting": lighting_var.get(),
            "HVAC": hvac_var.get(),
            "Insulation": insulation_var.get()
        }

        base_total = sum(BASE_USAGE.values())
        reduced_total = 0

        for system, base in BASE_USAGE.items():
            if upgrades[system]:
                reduced_total += base * (1 - SAVINGS[system])
            else:
                reduced_total += base

        saved = base_total - reduced_total
        percent = (saved / base_total) * 100

        base_label.config(text=f"Baseline Usage: {base_total:.0f} kWh/year")
        new_label.config(text=f"Estimated Usage: {reduced_total:.0f} kWh/year")
        savings_label.config(text=f"Energy Saved: {saved:.0f} kWh/year ({percent:.1f}%)")

    tk.Label(frame, text="Energy Efficiency Upgrade Simulator", font=("Arial", 20, "bold"), bg="#f7f9fa", fg="#2c3e50").pack(pady=20)
    input_frame = tk.Frame(frame, bg="#f7f9fa")
    input_frame.pack(pady=10, fill="x", padx=60)

    tk.Label(input_frame, text="Building Type:", font=("Arial", 14), bg="#f7f9fa").grid(row=0, column=0, sticky="w", pady=5)
    building_type_combo = ttk.Combobox(input_frame, font=("Arial", 14), state="readonly", values=["Residential", "Commercial", "Industrial"])
    building_type_combo.grid(row=0, column=1, pady=5, sticky="ew")
    building_type_combo.current(0)

    tk.Label(input_frame, text="Flow Area (m²):", font=("Arial", 14), bg="#f7f9fa").grid(row=1, column=0, sticky="w", pady=5)
    flow_area_entry = ttk.Entry(input_frame, font=("Arial", 14))
    flow_area_entry.grid(row=1, column=1, pady=5, sticky="ew")

    tk.Label(input_frame, text="Appliance Count:", font=("Arial", 14), bg="#f7f9fa").grid(row=2, column=0, sticky="w", pady=5)
    appliance_count_entry = ttk.Entry(input_frame, font=("Arial", 14))
    appliance_count_entry.grid(row=2, column=1, pady=5, sticky="ew")

    input_frame.columnconfigure(1, weight=1)
    options_frame = tk.Frame(frame, bg="#f7f9fa")
    options_frame.pack(pady=15)

    lighting_var = tk.BooleanVar()
    hvac_var = tk.BooleanVar()
    insulation_var = tk.BooleanVar()

    tk.Checkbutton(options_frame, text="Upgrade Lighting to LED", variable=lighting_var, font=("Arial", 14), bg="#f7f9fa").pack(anchor="w", pady=5)
    tk.Checkbutton(options_frame, text="Upgrade HVAC System", variable=hvac_var, font=("Arial", 14), bg="#f7f9fa").pack(anchor="w", pady=5)
    tk.Checkbutton(options_frame, text="Improve Insulation", variable=insulation_var, font=("Arial", 14), bg="#f7f9fa").pack(anchor="w", pady=5)

    ttk.Button(frame, text="Simulate Savings", command=calculate_savings).pack(pady=20)

    results_frame = tk.Frame(frame, bg="#f7f9fa")
    results_frame.pack(pady=10)

    base_label = tk.Label(results_frame, text="Baseline Usage: -", font=("Arial", 14), bg="#f7f9fa", fg="#333")
    base_label.pack(pady=5)

    new_label = tk.Label(results_frame, text="Estimated Usage: -", font=("Arial", 14), bg="#f7f9fa", fg="#333")
    new_label.pack(pady=5)

    savings_label = tk.Label(results_frame, text="Energy Saved: -", font=("Arial", 14, "bold"), bg="#f7f9fa", fg="green")
    savings_label.pack(pady=5)

    tk.Label(frame, text="ZESCO Efficiency Simulator | 2025", font=("Arial", 10), bg="#f7f9fa", fg="#999").pack(side="bottom", pady=10)

# ---------------- Main App ------------------
def update_canvas(text):
    if text == "Energy Audit":
        create_energy_audit_form(canvas2)
    elif text == "Net Metering":
        open_net_metering(canvas2)
    elif text == "Efficiency":
        open_efficiency(canvas2)
    else:
        canvas2.delete("all")
        canvas2.create_text(250, 75, text=f"You clicked: {text}", font=("Helvetica", 14))

root = tk.Tk()
root.title("Energy Dashboard")
root.geometry("800x600")

canvas1 = tk.Canvas(root, height=60, bg="lightgrey")
canvas1.pack(side="top", fill="x")

canvas2 = tk.Canvas(root, bg="white")
canvas2.pack(side="top", fill="both", expand=True)

button_labels = ["Energy Audit", "Efficiency", "Net Metering", "Results and Visualization"]

for i, label in enumerate(button_labels):
    btn = tk.Button(canvas1, text=label, command=lambda l=label: update_canvas(l))
    canvas1.create_window(100 + i * 170, 30, window=btn)

