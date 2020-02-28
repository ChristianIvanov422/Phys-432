# Phys 432: Assignment 4
## By: Christian Ivanov
### using Python 3.x

## list of files
### advection.py
compares two advaction solvers, one with the FTCS scheme and one with the Lax-Friedrich scheme. In both cases, dx = dt = 1 is used as well as u = -0.1

### advection-diffusion.py
modifies the Lax-Friedrich code from advection.py to also include diffusion, and runs it for two diffusion constants: D = 1 and D = 10

### Notes
From advection.py, we see that the FTCS scheme is unstable and rapidly explodes, while the Lax-Friedrich scheme is stable.

From advection-diffusion.py, we see that adding in diffusion "smoothes out" the curve, and that the larger the diffusion constant is, the smoother it gets.
