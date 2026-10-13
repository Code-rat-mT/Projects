import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook, load_workbook
import os

width = 800
height = 800

def create():
    def initialize_excel(file_name):
        """Create a new Excel file with headers if it doesn't exist."""
        if not os.path.exists(file_name):
            wb = Workbook()
            ws = wb.active
            ws.title = "Lighting Data"
            ws.append(["Lamps", "Bulb Rating", "Ballast Per Tube", "Lux (Lumens)", "Hours Per Day"])
            wb.save(file_name)

    def update_display(file_name):
        """Read Excel content and display it in the label."""
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

    # --- GUI Setup ---
    root = tk.Tk()
    root.title("Lighting Info Form")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))
    root.geometry(f"{width}x{height}+{x}+{y}")

    # Filename Entry
    tk.Label(root, text="Excel File Name:", font = 20 ).grid(row=0, column=0, padx=10, pady=5, sticky="w")
    filename_entry = tk.Entry(root, width=30, font=20)
    filename_entry.insert(0, "lighting_data.xlsx")
    filename_entry.grid(row=0, column=1, padx=10, pady=5)

    # Entry Fields
    labels = ["Room Name", "Lamps", "Bulb Rating", "Ballast Per Tube", "Lux (Lumens)", "Hours Per Day"]
    entries = []

    for i, label_text in enumerate(labels):
        label = tk.Label(root, text=label_text, font = 15)
        label.grid(row=i+2, column=0, padx=10, pady=5, sticky="w")
        
        entry = tk.Entry(root, width=30, font=20)
        entry.grid(row=i+1, column=1, padx=10, pady=5)
        entries.append(entry)

    room_name, lamps_entry, bulb_rating_entry, ballast_entry, lux_entry, hours_entry = entries

    # Submit Button
    submit_button = tk.Button(root, text="Submit", font=30, command=submit)
    submit_button.grid(row=len(labels)+1, column=0, columnspan=2, pady=15)

    # Display Label
    display_label = tk.Label(root, text="Excel contents will appear here.", justify="left", anchor="w", font=8)
    display_label.grid(row=len(labels)+2, column=0, columnspan=2, padx=10, pady=10, sticky="w")

    # Initial load of default file
    update_display("lighting_data.xlsx")

    root.mainloop()


def window():
    create()
