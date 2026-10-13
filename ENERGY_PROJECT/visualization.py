import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random

# Simulate hourly energy data
def simulate_data():
    hours = [f"{h}:00" for h in range(6, 19)]
    solar = [round(random.uniform(1, 5), 2) for _ in hours]
    consumption = [round(random.uniform(2, 4), 2) for _ in hours]
    export = [max(0, s - c) for s, c in zip(solar, consumption)]
    net = [c - s if c > s else 0 for s, c in zip(solar, consumption)]
    return hours, solar, consumption, export, net

# Initialize main window
def create():
    root = tk.Tk()
    root.title("Energy Data Visualization Dashboard")
    root.geometry("800x800")
    root.resizable(False, False)  # Lock window size
    root.configure(bg="#f0f4f8")

    tk.Label(root, text="Energy Profile Dashboard", font=("Arial", 18, "bold"),
            bg="#f0f4f8", fg="#2b3e50").pack(pady=10)

    # Frame for charts
    chart_frame = tk.Frame(root, bg="#f0f4f8")
    chart_frame.pack(fill="both", expand=True, padx=10, pady=5)

    # Simulated Data
    hours, solar, consumption, export, net = simulate_data()
    x = list(range(len(hours)))
    width = 0.2

    # Totals for Pie Chart
    total_solar = sum(solar)
    total_consumption = sum(consumption)
    total_export = sum(export)
    total_net = sum(net)

    # Create figure with 3 charts
    fig = plt.figure(figsize=(8, 7))  # Fit into 800x800 window

    # --- Bar Chart ---
    ax1 = fig.add_subplot(3, 1, 1)
    ax1.bar([i - 1.5 * width for i in x], solar, width=width, label="Solar", color="#4CAF50")
    ax1.bar([i - 0.5 * width for i in x], consumption, width=width, label="Consumption", color="#2196F3")
    ax1.bar([i + 0.5 * width for i in x], export, width=width, label="Export", color="#FFC107")
    ax1.bar([i + 1.5 * width for i in x], net, width=width, label="Net Import", color="#F44336")
    ax1.set_ylabel("kWh")
    ax1.set_title("Bar Chart - Hourly Energy Data", fontsize=10)
    ax1.legend(fontsize=8)
    ax1.grid(True, linestyle="--", alpha=0.3)

    # --- Line Chart ---
    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(x, solar, label="Solar", marker='o', color="#4CAF50")
    ax2.plot(x, consumption, label="Consumption", marker='o', color="#2196F3")
    ax2.plot(x, export, label="Export", marker='o', color="#FFC107")
    ax2.plot(x, net, label="Net Import", marker='o', color="#F44336")
    ax2.set_xticks(x)
    ax2.set_xticklabels(hours, rotation=45, fontsize=8)
    ax2.set_ylabel("kWh")
    ax2.set_title("Line Chart - Energy Trends", fontsize=10)
    ax2.legend(fontsize=8)
    ax2.grid(True, linestyle="--", alpha=0.3)

    # --- Pie Chart ---
    ax3 = fig.add_subplot(3, 1, 3)
    labels = ["Solar", "Consumption", "Export", "Net Import"]
    sizes = [total_solar, total_consumption, total_export, total_net]
    colors = ["#4CAF50", "#2196F3", "#FFC107", "#F44336"]
    ax3.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140, textprops={'fontsize': 8})
    ax3.set_title("Pie Chart - Total Energy Distribution", fontsize=10)

    fig.tight_layout(pad=2.5)

    # Embed chart in Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # Run the app
    root.mainloop()

def window():
    create()
    
