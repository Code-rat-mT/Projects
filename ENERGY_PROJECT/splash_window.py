import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import energy_audit as sp
import metering as met
import efficiency_1 as eff
import visualization as vis
import energy_audit1 as eg1
def energy():
    eg1.window()

def efficiency():
    eff.window()

def metering():
    pass
    met.window()

def visualization():
    vis.window()

def main_window():
    splash_root.destroy()
    main_window = tk.Tk()
    style = ttk.Style()
    style.configure("TButton", 
                background="lightblue", 
                foreground="black", 
                font=("Arial", 12), 
                padding=10,
                width = 40,
                hegiht =50)
    main_window.title("Main Window")
    main_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    main_window['bg'] = '#51856C'

    #We add a label
    
    label1 = tk.Label(main_window, text = "Welcome", font = ("Arial", 30))
    label1.pack(pady=100)
    
    button1 = ttk.Button(main_window, text = "Energy Audit", command = energy)
    button1.pack(pady = 5)

    button2 = ttk.Button(main_window, text = "Efficiecy Measures", command = efficiency)
    button2.pack(pady = 5)  

    button3 = ttk.Button(main_window, text = "Net Metering", command = metering)
    button3.pack(pady = 5)

    button4 = ttk.Button(main_window, text = "Results and Visualization", command = visualization)
    button4.pack(pady = 5)

    button5 = ttk.Button(main_window, text = "Exit", command = exit)
    button5.pack(pady = 5)

splash_root = tk.Tk()
splash_root.title("Splash Screen")
splash_root['bg'] = "#13570D"

splash_root.overrideredirect(True)

width = 800
height = 800

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = (screen_width/2) - (width/2)
y= (screen_height/2) - (height/2)

TEXT_COLOR1 = "#131424"
splash_root.geometry('%dx%d+%d+%d' % (width, height, x, y))


try:
    image1 = Image.open("ENERGY_PROJECT\pictures\house_energy.png")
    eiz_logo = Image.open("ENERGY_PROJECT\pictures\EIZ.png")
    unza_logo = Image.open("ENERGY_PROJECT/pictures/unza.png")
    photo = ImageTk.PhotoImage(image1)
    unza_photo = ImageTk.PhotoImage(unza_logo)
    
    label1 = tk.Label(splash_root, image=photo)
    label1.place(width=x+width/2, height =y+width)

    label2 = tk.Label(label1, text = "ENERGY AUDIT PROJECT", fg= TEXT_COLOR1, font = ("Helvetica", 25))
    label2.pack()

    eiz_photo = ImageTk.PhotoImage(eiz_logo)
    eiz_label = tk.Label(label1, image = eiz_photo)
    eiz_label.place(x=30, y = 50)

    
    unza_label = tk.Label(label1, image = unza_photo)
    unza_label.place(x=500, y =50)

    label3 = tk.Label(label1, text = "Starting...", fg= TEXT_COLOR1, font = ("Helvetica", 25, "italic"))
    label3.place(x=x-40, y = y+height-130)

    splash_root.photo = photo
    splash_root.eiz_photo = eiz_photo

    
except FileNotFoundError:
    tk.Label(splash_root, text = "Loading...", font = ("Helvetica", 16)).pack()

splash_root.after(5000, main_window)
splash_root.mainloop()

#Just the front end....The back end logic will be added after the presentation