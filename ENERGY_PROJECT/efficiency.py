import tkinter as tk
from tkinter import ttk, filedialog, messagebox

width = 800
height = 800

def create():
    def upload_csv():
        file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file:
            file_path.set(file)

    def submit_form():
        b_type = building_type.get()
        area = floor_area.get()
        count = appliance_count.get()
        file = file_path.get()
        messagebox.showinfo("Form Submitted", f"""
        Building Type: {b_type}
        Floor Area: {area} m²
        Appliance Count: {count}
        CSV File: {file}
        """)

    root = tk.Tk()
    root.title("Energy Audit Input")

    bg_color = "#51856C"  # Background color
    root.configure(bg=bg_color)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    frame = tk.Frame(root, bg=bg_color, padx=20, pady=20)
    frame.pack(pady=40, padx=20, fill=tk.BOTH, expand=True)

    label_style = {"bg": bg_color, "fg": "white"}
    entry_style = {"font": ("Helvetica", 20), "width": 60}

    # Title
    tk.Label(frame, text="Energy Audit Input", **label_style, font=("Helvetica", 18, "bold")).pack(anchor="w", pady=(0, 10))

    # Building Type
    tk.Label(frame, text="Building Type", **label_style, font=("Helvetica", 14, "bold")).pack(anchor="w")
    building_type = ttk.Combobox(frame, values=["Residential", "Commercial", "Industrial"], font=("Helvetica", 20), width=60)
    building_type.set("Select type")
    building_type.pack(pady=5)

    # Floor Area
    tk.Label(frame, text="Floor Area (m²)", **label_style, font=("Helvetica", 14, "bold")).pack(anchor="w")
    floor_area = tk.Entry(frame, **entry_style)
    floor_area.insert(0, "e.g., 150")
    floor_area.pack(pady=5)

    # Appliance Count
    tk.Label(frame, text="Appliance Count", **label_style, font=("Helvetica", 14, "bold")).pack(anchor="w")
    appliance_count = tk.Entry(frame, **entry_style)
    appliance_count.insert(0, "e.g., 12")
    appliance_count.pack(pady=5)

    # File Upload
    tk.Label(frame, text="Upload Load Profile (CSV)", **label_style, font=("Helvetica", 14, "bold")).pack(anchor="w")
    file_path = tk.StringVar()
    file_entry = tk.Entry(frame, textvariable=file_path, state="readonly", **entry_style)
    file_entry.pack(pady=5)
    tk.Button(frame, text="Choose File", command=upload_csv, bg="#406854", fg="white", font=("Helvetica", 10)).pack(anchor="e", pady=5)

    # Submit Button
    tk.Button(frame, text="Submit", command=submit_form, bg="#2F4F3F", fg="white", padx=10, pady=5,
              font=("Helvetica", 12)).pack(pady=20)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root['bg'] = '#51856C'
    root.mainloop()
    

def window():
    create()


