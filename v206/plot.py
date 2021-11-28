import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

t, T1, T2 = np.genfromtxt('temp.txt', unpack=True, skip_header=1)

# Nicht-lineare Ausgleichsfunktion
def f(x, a, b, c):
    return a* (x**2) + b*x + c

# curve fit
param1, pcov1 = curve_fit(f, t, T1)
param2, pcov2 = curve_fit(f, t, T2)
# Parameter zusammenfassen
a1, b1, c1 = param1
a2, b2, c2 = param2

unc1 = np.sqrt(np.diag(pcov1))
unc2 = np.sqrt(np.diag(pcov2))
fa1, fb1, fc1 = unc1
fa2, fb2, fc2 = unc2

# mu = 10**6
a1_mu = a1*10**6
a2_mu = a2*10**6
fa1_mu = fa1*10**6
fa2_mu = fa2*10**6

x = np.linspace(0, 2000, 500)
y1 = f(x, a1, b1, c1)
y2 = f(x, a2, b2, c2)
plt.plot(t, T1, '.r', label = "$T_{1}$")
plt.plot(t, T2, '.b', label = "$T_{2}$")
plt.plot(x, y1, '-r', label = "Ausgleichsparabel $T_{1}$")
plt.plot(x, y2, '-b', label = "Ausgleichsparabel $T_{2}$")
plt.xlabel(r'Zeit t(s)')
plt.ylabel(r'Temperatur (K)')
plt.legend(loc="best")

plt.savefig('build/plot.pdf')