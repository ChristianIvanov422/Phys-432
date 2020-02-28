import numpy as np
from matplotlib import pyplot as plt
import scipy.sparse.linalg as linalg

#defining all the variables
#will use 500 points for the plots
npoints = 500
u = -0.1
dt = 1
dx = 1
a = u*dt/(2*dx)
x = np.linspace(0,1,num=npoints)

#chosing the two diffusion coefficients
#also setting up the initial f(x)=x for both runs
D1 = 1
b1 = D1*dt/dx**2
f1 = x.copy()
D2 = 10
b2 = D2*dt/dx**2
f2 = x.copy()

#setting up the plots
plt.ion()
fig = plt.figure(figsize = [12,6])
ax1 = fig.add_subplot(121)
x1, = ax1.plot(x,f1,'b-')
ax1.set_title('D = 1')

ax2 = fig.add_subplot(122)
x2, = ax2.plot(x,f1,'r-')
ax2.set_title('D = 10')
fig.canvas.draw()

#will run the code for 3000 iterations
#it is enough to see what is going on
steps = 3000
for i in range(steps):
    #implementing the matrix to solve the diffusion implicitly
    A1 = np.eye(npoints)*(1+2*b1) - np.eye(npoints,k=1)*b1 - np.eye(npoints,k=-1)*b1
    #setting up so-slip boundary conditions on both ends
    #this is to prevent anything from escaping out of the system
    A1[0][0]=1
    A1[0][1]=0
    A1[-1][-1]=1
    A1[-1][-2]=0
    #note that the matrix is mostly sparse
    #thus, using conjugate gradient to solve the system significantly speeds things up
    f1 = linalg.cg(A1, f1)[0]
    f1[1:-2] = 0.5*(f1[2:-1]+f1[0:-3]) - a*(f1[2:-1]-f1[0:-3])
    
    #repeating the same thing for the second diffusion coefficient
    A2 = np.eye(npoints)*(1+2*b2) - np.eye(npoints,k=1)*b2 - np.eye(npoints,k=-1)*b2
    A2[0][0]=1
    A2[0][1]=0
    A2[-1][-1]=1
    A2[-1][-2]=0
    f2 = linalg.cg(A2, f2)[0]
    f2[1:-2] = 0.5*(f2[2:-1]+f2[0:-3]) - a*(f2[2:-1]-f2[0:-3])
    #plotting once every 50 iterations to speed things up
    if i%50 == 0:
        x1.set_ydata(f1)
        x2.set_ydata(f2)
        fig.canvas.draw()
        plt.pause(0.001)