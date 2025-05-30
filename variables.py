b = 17 #span (m)
S = 27 #wing surface (m^2)
m = 5100 #total mass (kg)
W = m*9.8 #weight
fuel = 0.2*m # % of fuell from total mass (kg)

#lift
Cl_0 = 0.12
Cl_a = 0.09
a_s = 14.2 #stall angle of attack (º)
a = 0 #initial valor
Cl_aoa = Cl_0+Cl_a*a #lift coeficient form angle of atac

#drag
Cd_0 = 0.019
k = 0.11

#flight conditions at sea level
h_SL = 0 #height (m)
p_SL = 1.225 #air density (kg/m^3)
t_SL = 288.15 # temperature (k)

#flight conditions at cruising altitude
h_CR = 11000
p_CR = p_SL/3
t_CR = 221.75

#turbo get engines
Ta_SL = 18100 #available trust at sea level (N)

#turboporp engines
Pa_SL = 1.1*10**6 #combined power (W)


