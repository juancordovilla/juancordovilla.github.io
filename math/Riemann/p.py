import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameter values
initial_s = 1.0
initial_w = 1.0

# Create a figure and axis
fig, ax = plt.subplots(3, 1)

# Generate initial x values
#n_values = np.linspace(0.1, 5, 100)
n_values = np.arange(1,100)

# Initial y values for the functions
y_values1 = 1 / n_values**initial_s
y_values2 = np.sin(initial_w * n_values)
y_values3 = np.cos(initial_w * n_values)

# Plot the initial graphs
line1, = ax[0].plot(n_values, y_values1)
line2, = ax[1].plot(n_values, y_values2)
line3, = ax[2].plot(n_values, y_values3)

# Add sliders for the parameters 'a'
ax_slider1 = plt.axes([0.25, 0.97, 0.65, 0.03])
ax_slider2 = plt.axes([0.25, 0.02, 0.65, 0.03])

slider_s = Slider(ax_slider1, 'Parameter s', 0.1, 2.0, valinit=initial_s)
slider_w = Slider(ax_slider2, 'Parameter w', 0.1, 200.0, valinit=initial_w)

# Function to update the plots when the sliders are changed
def update(val):
    s = slider_s.val
    w = slider_w.val
    w2 = math.ceil(2*w)

    # Generate initial x values
    n_values2 = np.arange(1,w2)

    # Update the y values for the functions
    fs=1 / n_values**s
    fw=np.sin(w2 * np.log(n_values))
    fsw=fs*fw
    
    line1.set_ydata(fs)
    line2.set_ydata(fw)
    line3.set_ydata(n_values2)

# Attach the update function to the sliders
slider_s.on_changed(update)
slider_w.on_changed(update)

# Show the plot
plt.show()
