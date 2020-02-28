"""
Advection equation: FTCS vs Lax-Fredrich schemes

@author: Christian Ivanov
28/02/2020
"""

import numpy as np
from matplotlib import pyplot as plt

#defining all the variables
#will use 500 points for the plots
npoints = 500
u = -0.1
dt = 1
dx = 1
a = u*dt/(2*dx)
#setting up the initial f(x)=x for x between 0 and 1
#f1 is for FTCS, f2 for Lax-Fredrich
x = np.linspace(0,1,num=npoints)
f1 = x.copy()
f2 = x.copy()

#setting up the plots
plt.ion()
fig = plt.figure(figsize = [12,6])
ax1 = fig.add_subplot(121)
#we expect FTCS to be unstable, so we set a y-limit on the plot
plt.ylim((-0.1,1.1))
x1, = ax1.plot(x,f1,'b.')
ax1.set_title('FTCS')

ax2 = fig.add_subplot(122)
x2, = ax2.plot(x,f1,'r.')
ax2.set_title('Lax-Friedrich')
fig.canvas.draw()

#will run the code for 3000 iterations
#it is enough to see what is going on
steps = 3000
for i in range(steps):
    #implementing the FTCS scheme
    f1[1:-2] = f1[1:-2] - a*(f1[2:-1]-f1[0:-3])
    #implementing the Lax-Fredrich scheme
    f2[1:-2] = 0.5*(f2[2:-1]+f2[0:-3]) - a*(f2[2:-1]-f2[0:-3])
    #plotting once every 10 iterations to speed things up
    if i%10 == 0:
        x1.set_ydata(f1)
        x2.set_ydata(f2)
        fig.canvas.draw()
        plt.pause(0.001)