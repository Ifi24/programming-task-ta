import matplotlib.pyplot as plt

# Constants
b = 17
S = 27
m = 5100
W = m * 9.8
Cd_0 = 0.019
k = 0.11

# Air densities
rho_SL = 1.225
rho_CR = rho_SL / 3
rho_bar = rho_CR / rho_SL  # = 1/3

# Drag constants
A = 0.5 * rho_SL * S * Cd_0
B = 2 * k / (rho_SL * S)

# Engine limits
T_available = 18100         # N
P_available = 1.1 * 10**6   # W

# Ranges
V_vals = range(10, 400)
T_vals = []
P_vals = []

for V in V_vals:
    T = A * rho_bar * V**2 + B * W**2 / (rho_bar * V**2)
    P = T * V
    T_vals.append(T)
    P_vals.append(P)

# Points of interest
min_T = min(T_vals)
min_P = min(P_vals)
V_range = V_vals[T_vals.index(min_T)]
V_endurance = V_vals[P_vals.index(min_P)]

# Plot
plt.figure(figsize=(12, 6))

# Thrust Required
plt.subplot(1, 2, 1)
plt.plot(V_vals, T_vals, label='Thrust Required')
plt.axhline(T_available, color='gray', linestyle='--', label='Thrust Available')
plt.scatter(V_range, min_T, color='red', label='Max Range')
plt.xlabel('Airspeed (m/s)')
plt.ylabel('Thrust Required (N)')
plt.title('Thrust Required vs Airspeed')
plt.ylim(0, T_available * 1.1)
plt.legend()
plt.grid(True)

# Power Required
plt.subplot(1, 2, 2)
plt.plot(V_vals, P_vals, label='Power Required', color='green')
plt.axhline(P_available, color='gray', linestyle='--', label='Power Available')
plt.scatter(V_endurance, min_P, color='orange', label='Max Endurance')
plt.xlabel('Airspeed (m/s)')
plt.ylabel('Power Required (W)')
plt.title('Power Required vs Airspeed')
plt.ylim(0, P_available * 1.1)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Print key results
print(f"Max Range (Turbojet) at V = {V_range} m/s")
print(f"Max Endurance (Turboprop) at V = {V_endurance} m/s")