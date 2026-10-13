import tkinter as tk
from PIL import Image, ImageTk

# Define colors
TEXT_COLOR1 = "#003366"  # example color

# Create root window
splash_root = tk.Tk()
splash_root.geometry("800x600")  # Adjust as needed

# Load and display images (keep references!)
image1 = Image.open("ENERGY_PROJECT/pictures/house_energy.png")
eiz_logo = Image.open("ENERGY_PROJECT/pictures/EIZ.png")

photo = ImageTk.PhotoImage(image1)
eiz_photo = ImageTk.PhotoImage(eiz_logo)

# Store references to prevent garbage collection
splash_root.photo = photo
splash_root.eiz_photo = eiz_photo

# Create main image label
label1 = tk.Label(splash_root, image=photo)
label1.place(x=0, y=0, relwidth=1, relheight=1)

# Overlay text
label2 = tk.Label(label1, text="ENERGY AUDIT PROJECT", fg=TEXT_COLOR1, bg="white", font=("Helvetica", 25))
label2.pack(pady=10)

# Add second logo image
eiz_label = tk.Label(label1, image=eiz_photo, bg="white")
eiz_label.pack(pady=20)

# Start the GUI
splash_root.mainloop()
