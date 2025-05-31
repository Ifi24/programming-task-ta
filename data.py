b = 17 #span (m)
S = 27 #wing surface (m^2)
m = 5100 #total mass (kg)
fuel = 0.2*m # % of fuell from total mass (kg)
g = 9.81 #gravity
W = m * g #weight (kg)

#lift
CL0 = 0.12
CLAlpha = 0.09
Alpha_s = 14.2 #stall angle of attack (º)

#drag
CD0 = 0.019
k = 0.11

#flight conditions at sea level
h_SL = 0 #height (m)
p_SL = 1.225 #air density (kg/m^3)
t_SL = 288.15 # temperature (k)

#flight conditions at cruising altitude
h_CR = 11000
p_CR = p_SL/3
t_CR = 221.75

partialPressure = p_CR/p_SL #partial pressure

#turbojet engines
Ta_SL = 18100 #available trust at sea level (N)

#turboporp engines
Pa_SL = 1.1*10**6 #combined power (W)

# Aerodynamic functions
def getCL(alpha):
    return CL0 + (CLAlpha*alpha)

def getCD(alpha):
    CL = getCL(alpha)
    return CD0 + (k*(CL**2))

# parameters
A = 0.5 * p_SL * S * CD0
B = (2 * k)/(p_SL * S)