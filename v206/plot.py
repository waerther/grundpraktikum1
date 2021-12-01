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
plt.plot(t, T1, '^r', label = "$T_{1}$")
plt.plot(t, T2, 'vb', label = "$T_{2}$")
plt.plot(x, y1, '-r', label = "Ausgleichsparabel $T_{1}$")
plt.plot(x, y2, '-b', label = "Ausgleichsparabel $T_{2}$")
plt.xlabel(r'Zeit t(s)')
plt.ylabel(r'Temperatur (K)')
plt.legend(loc="best")
plt.grid(True)

plt.savefig('build/plot1.pdf')

plt.clf() # clears plot


messdaten = pd.read_excel("messdaten.xlsx")
pb = messdaten.iloc[:,[4, 9]] 
np.savetxt('pb.txt', pb.values, header='T1(K) p_b(Pa)', fmt='%f')
T1, pb = np.genfromtxt('pb.txt', unpack=True, skip_header=1)
rT1 = 1/T1
p0 = pb[0]
xx = rT1
yy = np.log((pb/p0))
plt.plot(xx, yy, 'vb')

# Nicht-lineare Ausgleichsfunktion
def g(x, a, b):
    return a * x + b

para, pcov = curve_fit(g, rT1, yy)
pcov = np.sqrt(np.diag(pcov))
para = np.round(para, 3)
pcov = np.round(pcov, 3)
a, b = para
fa, fb = pcov  
R = 8.3144508

dreg = {'Wert': para, 'Fehler': pcov}
dfreg = pd.DataFrame(data = dreg, index = ['Steigung m', 'Achsenabschnitt b'])
print(dfreg.to_latex(index = True, column_format= "c c c"))
plt.plot(rT1, g(rT1, a, b), '-b')

plt.xlabel(r'$\frac{1}{T_{1}}$ ($\frac{1}{s}$)')
plt.ylabel(r'ln($\frac{p_{b}}{p_{0}}$)')

plt.grid(True)
plt.savefig('build/plot2.pdf', bbox_inches = "tight") # damit das label nicht abgeschnitten wird
plt.clf()
