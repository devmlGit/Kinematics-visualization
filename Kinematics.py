import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import *

"""
--------------- Velocity and acceleration -----------------
Author: Mounir LBATH
Version: 1.0
Creation Date: 12/2020
-----------------------------------------------------------
"""
vectorLength = 0.15

# Parametric curves to be defined here (after "lambda t :" )
x = lambda t : sin(2*t) #<--- x(t)
y = lambda t : cos(3*t) #<--- y(t)
z = lambda t : sin(4*t) #<--- z(t)

#########################################################

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

#################################
######### Functions #############
#################################

# Domain
s = 0.01 #precision
D=np.arange(0.0,2*pi,s)



# Calculate points
xcoord=[]
ycoord=[]
zcoord=[]
for t in D:
    xcoord.append(x(t))
    ycoord.append(y(t))
    zcoord.append(z(t))

# Derivative of f (function lambda) in a (real)
h = 0.001  #derivative precision
d = lambda f,a : (f(a+h)-f(a))/h  #simple derivative
dd = lambda f,a : (d(f,a+h)-d(f,a))/h  #double derivative

#################################
######### Velocity ##############
#################################
    
# Initial Velocity vector
def get_velocity(t):
    return x(t),y(t),z(t),d(x,t),d(y,t),d(z,t)

velocity = ax.quiver(*get_velocity(0),length = vectorLength, color=(0.75,0,0), arrow_length_ratio=0.2)

# Animate speed vector
precision = 0.01 #animation precision
def updateVelocity(theta):
    global velocity
    velocity.remove()
    velocity = ax.quiver(*get_velocity(theta*precision), length = vectorLength, color=(0.75,0,0),arrow_length_ratio=0.2)

#################################
####### Acceleration ############
#################################
    
# Initial Velocity vector
def get_accel(t):
    return x(t),y(t),z(t),dd(x,t),dd(y,t),dd(z,t)

accelLength = vectorLength/3
acceleration = ax.quiver(*get_accel(0),length = accelLength, color=(0,0.75,0), arrow_length_ratio=0.2)

# Animate speed vector
precision = 0.01 #animation precision
def updateAccel(theta):
    global acceleration
    acceleration.remove()
    acceleration = ax.quiver(*get_accel(theta*precision), length = accelLength, color=(0,0.75,0),arrow_length_ratio=0.2)

#################################
############# Plot ##############
#################################

# Velocity    
aniVelocity = FuncAnimation(fig, updateVelocity, interval=25)

# Acceleration    
aniAccel = FuncAnimation(fig, updateAccel, interval=25)

# Parametric curve
ax.plot(xcoord,ycoord,zcoord)

# Show
plt.show()
