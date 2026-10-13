import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd

width = 800
height = 800

def create():

    def analyze_energy():
        try:
            floor_area = float(floor_area_entry.get())
            occupants = int(occupants_entry.get())
            building_type = building_type_combo.get()
            hvac_type = hvac_type_combo.get()

            total_load = 0
            for item in tree.get_children():
                val = tree.set(item, "Load (kW)").strip()
                if val:
                    load = float(val)
                    if load < 0:
                        raise ValueError("Load cannot be negative")
                    total_load += load

            daily_consumption = total_load  # kWh/day assuming loads are average power per hour
            annual_consumption = daily_consumption * 365

            summary = (f"Building Type: {building_type}\n"
                    f"Floor Area: {floor_area} m²\n"
                    f"Occupants: {occupants}\n"
                    f"HVAC System: {hvac_type}\n"
                    f"Estimated Daily Energy Consumption: {daily_consumption:.2f} kWh\n"
                    f"Estimated Annual Energy Consumption: {annual_consumption:.2f} kWh")

            result_label.config(text=summary, fg="#116466")
        except ValueError as e:
            result_label.config(text=f"Input error: {e}", fg="red")

    def load_excel_file():
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls")])
        if file_path:
            try:
                df = pd.read_excel(file_path)
                display_excel(df)
            except Exception as e:
                result_label.config(text=f"Error loading Excel: {e}", fg="red")

    def display_excel(df):
        for widget in excel_frame.winfo_children():
            widget.destroy()

        x_scroll = tk.Scrollbar(excel_frame, orient="horizontal")
        y_scroll = tk.Scrollbar(excel_frame, orient="vertical")

        excel_tree = ttk.Treeview(excel_frame, columns=list(df.columns), show="headings",
                                  xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)
        x_scroll.config(command=excel_tree.xview)
        y_scroll.config(command=excel_tree.yview)

        x_scroll.pack(side="bottom", fill="x")
        y_scroll.pack(side="right", fill="y")
        excel_tree.pack(fill="both", expand=True)

        for col in df.columns:
            excel_tree.heading(col, text=col)
            excel_tree.column(col, anchor="center", width=100)

        for _, row in df.iterrows():
            excel_tree.insert("", "end", values=list(row))

    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    root.title("Building Energy Consumption Analysis")
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.configure(bg="#f0f4f8")

    tk.Label(root, text="Building Energy Consumption Dashboard", font=("Arial", 20, "bold"),
            bg="#f0f4f8", fg="#1a2935").pack(pady=15)

    building_frame = tk.LabelFrame(root, text="Building Energy Characteristics",
                                font=("Arial", 14), bg="#f0f4f8", fg="#1a2935", padx=10, pady=10)
    building_frame.pack(fill="x", padx=20, pady=10)

    excel_button = ttk.Button(root, text="Load Excel File", command=load_excel_file)
    excel_button.pack(pady=10)

    tk.Label(building_frame, text="Building Type:", font=("Arial", 12), bg="#f0f4f8").grid(row=0, column=0, sticky="w", pady=5)
    building_type_combo = ttk.Combobox(building_frame, values=["Residential", "Commercial", "Industrial"], state="readonly", font=("Arial", 12))
    building_type_combo.grid(row=0, column=1, pady=5, sticky="ew")
    building_type_combo.current(0)

    tk.Label(building_frame, text="Floor Area (m²):", font=("Arial", 12), bg="#f0f4f8").grid(row=1, column=0, sticky="w", pady=5)
    floor_area_entry = ttk.Entry(building_frame, font=("Arial", 12))
    floor_area_entry.grid(row=1, column=1, pady=5, sticky="ew")

    tk.Label(building_frame, text="Number of Occupants:", font=("Arial", 12), bg="#f0f4f8").grid(row=2, column=0, sticky="w", pady=5)
    occupants_entry = ttk.Entry(building_frame, font=("Arial", 12))
    occupants_entry.grid(row=2, column=1, pady=5, sticky="ew")

    tk.Label(building_frame, text="HVAC System Type:", font=("Arial", 12), bg="#f0f4f8").grid(row=3, column=0, sticky="w", pady=5)
    hvac_type_combo = ttk.Combobox(building_frame, values=["None", "Central AC", "Split AC", "Heating Only"], state="readonly", font=("Arial", 12))
    hvac_type_combo.grid(row=3, column=1, pady=5, sticky="ew")
    hvac_type_combo.current(0)

    building_frame.columnconfigure(1, weight=1)

    load_frame = tk.LabelFrame(root, text="Hourly Load Profile (kW)",
                            font=("Arial", 14), bg="#f0f4f8", fg="#1a2935", padx=10, pady=10)
    load_frame.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(load_frame, text="Enter estimated or metered hourly loads for 24 hours:",
            font=("Arial", 12), bg="#f0f4f8").pack(anchor="w", pady=5)

    columns = ("Hour", "Load (kW)")
    tree = ttk.Treeview(load_frame, columns=columns, show="headings", height=10)
    tree.heading("Hour", text="Hour")
    tree.heading("Load (kW)", text="Load (kW)")
    tree.column("Hour", width=100, anchor="center")
    tree.column("Load (kW)", width=150, anchor="center")

    for h in range(24):
        tree.insert("", "end", values=(f"{h}:00", ""))

    tree.pack(fill="both", expand=True)

    scrollbar = ttk.Scrollbar(load_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    result_frame = tk.Frame(root, bg="#f0f4f8")
    result_frame.pack(fill="x", padx=20, pady=10)

    analyze_btn = ttk.Button(result_frame, text="Analyze Energy Consumption", command=analyze_energy)
    analyze_btn.pack(pady=10)

    result_label = tk.Label(result_frame, text="", font=("Arial", 14), bg="#f0f4f8", fg="#116466")
    result_label.pack()

    # Load Excel section
   

    excel_frame = tk.Frame(root, bg="#f0f4f8", height=200)
    excel_frame.pack(fill="both", expand=True, padx=20, pady=10)

    root.mainloop()

def window():
    create()