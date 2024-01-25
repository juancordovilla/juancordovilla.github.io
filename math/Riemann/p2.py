import math
import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_plot(value):
    size = int(float(value))+1
    vector = np.arange(1,size)
    f1=np.sin(vector)
    print(f1)
    ax.clear()
    ax.plot(f1)  
    canvas.draw()

# Create the main application window
root = tk.Tk()
root.title("Interactive Vector Plotter")

# Create a slider
slider_label = ttk.Label(root, text="Vector Size:")
slider_label.pack(pady=10)
slider = ttk.Scale(root, from_=1, to=100, orient="horizontal", command=update_plot)
slider.set(10)  # Initial size of the vector
slider.pack()

# Create a Matplotlib Figure and set up the plot
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Initialize the plot with the default size
update_plot(slider.get())

# Run the Tkinter event loop
root.mainloop()

