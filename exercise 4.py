import matplotlib.pyplot as plt
import numpy as np
from data import *
from math import *

# Maximum glide distance velocity
V_BG = pow(((B * W**2)/(A * (partialPressure**2))), 1/4)

# Maximum glide time velocity
V_MS = pow(((B * W**2)/(3 * A * (partialPressure**2))), 1/4)

# The ROD formula as a function
def getROD(V):
    #Tr = -(A * partialPressure * (V**2) + B * ((W**2)/partialPressure * (V**2)))
    #ROD = (Tr * V)/W
    term1 = (A * partialPressure * V**3) / W
    term2 = B * W / (partialPressure * V)
    return -(term1 + term2)

# Creating the plot
airspeeds = range(60, 250, 1)
RODs = []
for airspeed in airspeeds:
    RODs.append(getROD(airspeed))

plt.figure()
plt.plot(airspeeds, RODs)
plt.xlabel('Airspeed [m/s]')
plt.ylabel('Sink rate (ROD) [m/s]')
plt.plot(V_BG, getROD(V_BG), 'ro', 
         label=f'Maximum Glide Distance ({V_BG:.3f} m/s)', 
         markersize=7)
plt.plot(V_MS, getROD(V_MS), 'go', 
         label=f'Maximum Glide Time ({V_MS:.3f} m/s)', 
         markersize=7)
plt.title('Sink rate vs Airspeed graph')
plt.grid()
plt.legend()
plt.show()