import matplotlib.pyplot as plt
from variables import*
import math

#variables d'aquest exercici
A=0.5*p_SL*S*Cd_0
B=2*k/(p_SL*S)
C=p_CR/p_SL
print(A,B,C)

#intervals dels grafics
initial_t = 50
final_t = 430
initial_p = 40
final_p = 215
print(initial_t,final_t,initial_p,final_p)

#eixos del grafic
valors_v_t = range(initial_t,final_t) #variable x en thrust
valors_t = [] #variable y in required thrust
valors_t_lift_induced = []
valors_t_zero_lift = []

valors_v_p = range(initial_p,final_p) #variable x en power
valors_p = [] #variable y in required power
valors_p_lift_induced = []
valors_p_zero_lift = []

for v in valors_v_t:
    #afegir valors del grafic de thrust
    t_lift_induced = B*W**2/(C*v**2)
    t_zero_lift = A*C*v**2
    t = t_zero_lift + t_lift_induced

    valors_t_lift_induced.append(t_lift_induced)
    valors_t_zero_lift.append(t_zero_lift)
    valors_t.append(t)

for v in valors_v_p:
    #afegir valors del grafic de power
    p_lift_induced = B * W ** 2 / (C * v)
    p_zero_lift = A * C * v ** 3
    p = p_zero_lift + p_lift_induced

    valors_p_lift_induced.append(p_lift_induced)
    valors_p_zero_lift.append(p_zero_lift)
    valors_p.append(p)

#dibuixar grafic
plt.figure(figsize=(12, 6))

#grafic del thrust
plt.subplot(1, 2, 1)
plt.plot(valors_v_t, valors_t_zero_lift, label="Zero-Lift",color = "orange", linewidth = 1.5)
plt.plot(valors_v_t, valors_t_lift_induced, label="Lift induced",color = "green",linewidth = 1.5)
plt.plot(valors_v_t, valors_t, label="Thrust Required",linewidth = 3)
plt.axhline(Ta_SL,label = "Aviable thrust",color = "gray",linestyle="--",linewidth = 1.5)
plt.title("Thrust Required vs Airspeed")
plt.xlabel('Airspeed V (m/s)')
plt.ylabel('Required Thrust (N)')
plt.legend(loc="best")
plt.grid(True)

#gràfic del power
plt.subplot(1, 2, 2)
plt.plot(valors_v_p, valors_p_zero_lift, label="Zero-Lift",color = "orange", linewidth = 1.5)
plt.plot(valors_v_p, valors_p_lift_induced, label="Lift induced",color = "green",linewidth = 1.5)
plt.plot(valors_v_p, valors_p, label="Thrust Required",linewidth = 3)
plt.axhline(Pa_SL,label = "Aviable thrust",color = "gray",linestyle="--",linewidth = 1.5)
plt.title("Thrust Required vs Airspeed")
plt.xlabel('Airspeed V (m/s)')
plt.ylabel('Required Thrust (N)')
plt.legend(loc="best")
plt.grid(True)

plt.show()

