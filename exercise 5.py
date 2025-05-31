import matplotlib.pyplot as plt
import numpy as np
from data import *
from math import *

# Maximum glide distance velocity
V_BG = pow(((B * W**2)/(A * (partialPressure**2))), 1/4)

# Minimum glide angle vs airspeed formula
def getGamma(V):
    term1 = (A * partialPressure * (V**2)) / W
    term2 = (B * W) / (partialPressure * (V**2))
    gamma = degrees(asin(-(term1 + term2)))
    return gamma

# Plotting the graphs
airspeeds = range(60, 250, 1)
Gammas = []
LDratios = []
for airspeed in airspeeds:
    Gammas.append(getGamma(airspeed))

# Minimum glide angle graph
plt.figure()
plt.plot(airspeeds, Gammas)
plt.xlabel('Airspeed [m/s]')
plt.ylabel('Minimum Glide Angle [degrees]')
plt.plot(V_BG, getGamma(V_BG), 'go',
         label=f'Minimum Glide Angle for Best Glide ({V_BG:.3f} m/s)',
         markersize=7)
plt.title('Minimum Glide Angle vs Airspeed graph')
plt.grid()
plt.legend()
plt.show()
