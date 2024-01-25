import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider 
from mpmath import zetazero, zeta


#tkinter is other option but bottleneck is line.set_data, without it is very fast


#Plt>Figure>ax>line: fig in plt, ax in fig, line in ax
fig, ax = plt.subplots(4,1) 

 


#Axis 
ax0=ax[0]
line0, = ax0.plot(1,2) 
ax1=ax[1]
line1, = ax[1].plot(1,2) 
ax2=ax[2]
line2, = ax[2].plot(1,2) 
ax3=ax[3]
sc = ax[3].scatter([1,-1],[-1,1]) 


#ax3=ax[3]
#line3, = ax[3].scatter(np.array[1,1],np.array[2,1]) 



#Slider in plt
ax_slider1 = plt.axes([0.25, 0.97, 0.65, 0.03])
ax_slider2 = plt.axes([0.25, 0.02, 0.65, 0.03])

slider_s = Slider(ax_slider1, 'Parameter s', 0.1, 2.0, valinit=1.0)
slider_w = Slider(ax_slider2, 'Parameter w', 0.1, 200.0, valinit=1.0)



def update(value):
    s = slider_s.val
    w = slider_w.val
    
    N = int(float(2*w))+2
    x = np.arange(1,N)
    ys=np.sin(w*np.log(x))
    yc=np.cos(w*np.log(x))
    ya=1 / x**s
    
    yca=ya*yc
    ysa=ya*ys
    z=np.sum(yca)+1j*np.sum(ysa)
    zo=zeta(s+1j*w)
    
    print(z,zo)
   
    
    #
    #ax.cla()
    #ax.plot(y1)
    #
    ax0.axis([0,N,-1,1])
    line0.set_data(x,ya)
    
    ax1.axis([0,N,-1,1])
    line1.set_data(x,ys)
    
    
    ax2.axis([0,N,-1,1])
    line2.set_data(x,ysa)
    
    
   
    y2d=np.array([yca,ysa])
    y2dd=y2d.transpose()
    sc.set_offsets(y2dd)    
    #print(ya)
        
slider_s.on_changed(update)
slider_w.on_changed(update)
plt.show()










