from data import *
from math import *

# Convert wind from knots to m/s (1 knot = 0.5144 m/s)
wind_speed = 25 * 0.5144  # 12.86 m/s
hw = -wind_speed    # negative for headwind
tw = wind_speed     # positive for tw

# Endurance and velocities from the document
E_jet = 0.224       # seconds (turbojet endurance)
V_jet_end = 147.49  # m/s (turbojet endurance velocity)
E_prop = 0.0017     # seconds (turboprop endurance)
V_prop_end = 112.07 # m/s (turboprop endurance velocity)

# Maximum range with wind adjustments
R_jet_head = E_jet * (V_jet_end + hw)
R_jet_tail = E_jet * (V_jet_end + tw)
R_prop_head = E_prop * (V_prop_end + hw)
R_prop_tail = E_prop * (V_prop_end + tw)

# Turbojet
Tr_min = 2 * W * sqrt(A * B)  # minimum required thrust
sin_gamma_max_jet = (Ta_SL - Tr_min) / W
gamma_max_jet = degrees(asin(sin_gamma_max_jet))  # in degrees

def T_R(V, p_bar=1.0):
    return A * p_bar * V**2 + (B * W**2) / (p_bar * V**2)

# Optimising over velocities to find max climb angle for the turboprop
best_excess = -float('inf')
best_V = 0
V_step = 0.1
V_current = 50
while V_current <= 300:
    thrust_avail = Pa_SL / V_current
    thrust_req = T_R(V_current)
    excess_thrust = thrust_avail - thrust_req
    excess_per_weight = excess_thrust / W
    if excess_per_weight > best_excess:
        best_excess = excess_per_weight
        best_V = V_current
    V_current += V_step

gamma_max_prop = degrees(asin(best_excess))

# Minimum angle of descent (glide) at cruising altitude
V_BG = (B * W**2 / (A * partialPressure**2))**0.25  # best glide speed

def get_drag(V, p_bar):
    return A * p_bar * V**2 + (B * W**2) / (p_bar * V**2)

# Headwind adjusted glide (wind is negative for hw)
V_head_glide = V_BG - hw
D_head = get_drag(V_head_glide, partialPressure)
sin_gamma_head = -D_head / W
gamma_head = degrees(asin(sin_gamma_head))

# Tailwind adjusted glide
V_tail_glide = V_BG - tw
D_tail = get_drag(V_tail_glide, partialPressure)
sin_gamma_tail = -D_tail / W
gamma_tail = degrees(asin(sin_gamma_tail))

# Results
print("Turbojet Results:")
print(f"Max Range (Headwind): {R_jet_head:.2f} m")
print(f"Max Range (Tailwind): {R_jet_tail:.2f} m")
print(f"Max Angle of Climb: {gamma_max_jet:.2f} degrees")
print(f"Min Angle of Descent (Headwind): {gamma_head:.2f} degrees")
print(f"Min Angle of Descent (Tailwind): {gamma_tail:.2f} degrees")
print("\nTurboprop Results:")
print(f"Max Range (Headwind): {R_prop_head:.4f} m")
print(f"Max Range (Tailwind): {R_prop_tail:.4f} m")
print(f"Max Angle of Climb: {gamma_max_prop:.2f} degrees")
print(f"Min Angle of Descent (Headwind): {gamma_head:.2f} degrees")
print(f"Min Angle of Descent (Tailwind): {gamma_tail:.2f} degrees")