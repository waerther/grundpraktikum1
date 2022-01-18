import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray
from uncertainties import unumpy as unp 


# plot1 

Uc, T = np.genfromtxt('tables/a.txt', unpack=True, skip_header=1)

# lineare Ausgleichsfunktion
def f(t, a, b):
    return a * t + b

y = np.log(Uc/Uc[0])

para, pcov = curve_fit(f, T, y)
pcov = np.sqrt(np.diag(pcov))
a, b = para
fa, fb = pcov 

plt.plot(T, y, 'xr', markersize=6 , label = 'Messwerte', alpha=0.5)
xx = np.linspace(-10, 140)
plt.plot(xx, f(xx, a, b), '-b', linewidth = 1, label = 'Ausgleichsgerade')

plt.xlabel(r'$t \, / \, \mathrm{\mu s}$')
plt.ylabel(r'$\ln \left(\frac{U_\mathrm{c}}{U_{0}}\right)$')
plt.legend(loc="best")
plt.grid(True)
plt.xlim(-5, 135)

ua = ufloat(a, fa)
RC = -1/ua

plt.savefig('build/plot1.pdf')
plt.clf() 


#plot 2
f, Uc = np.genfromtxt('tables/b.txt', unpack=True, skip_header=1)

Uc = Uc/Uc[0]
# Ausgleichsfunktion
def g(f, T):
    w = 2 * np.pi * f
    return 1 / (np.sqrt(1 + w**2 * T**2))

para, pcov = curve_fit(g, f, Uc)
pcov = np.sqrt(np.diag(pcov))
a = para
print(a)
fa = pcov 

plt.plot(f, Uc, 'xr', markersize=6 , label = 'Messwerte', alpha=0.5)
xx = np.linspace(100, 150000, 10**4)
plt.plot(xx, g(xx, a), '-b', linewidth = 1, label = 'Ausgleichsfunktion')

plt.xlabel(r'$f \, / \, \mathrm{Hz}$')
plt.ylabel(r'$A(\omega) \, / \, U_0$')
plt.xscale('log')
plt.legend(loc="best")
plt.grid(True)
plt.xlim(200, 150000)

plt.savefig('build/plot2.pdf')
plt.clf() 


# plot 3
f, Uc, a = np.genfromtxt('tables/c.txt', unpack=True, skip_header=1)
a *= 1e-6
b = 1/f
phi = 2 * np.pi * a/b

def phase(f, T):
    omega = 2 * np.pi * f
    return np.arctan(-1 * omega * T)

para, pcov = curve_fit(phase, f, phi)
pcov = np.sqrt(np.diag(pcov))
a = para
fa = pcov 

plt.plot(f, phi, 'xr', markersize=6 , label = 'Messwerte', alpha=0.5)
xx = np.linspace(100, (3)*1e5, 100000)
plt.plot(xx, phase(xx, a), '-b', linewidth = 1, label = 'Ausgleichsgerade')

plt.xlabel(r'$f \, / \, \mathrm{Hz}$')
plt.ylabel(r'$\phi \, / \, \mathrm{rad}$')
plt.legend(loc="best")
plt.xscale('log')
plt.grid(True)
plt.xlim(100, (2)*1e5)

plt.savefig('build/plot3.pdf')
plt.clf() 

# polarplot 
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.scatter(phi, g(f, noms(RC)*1e-6), marker='+', linewidth=1, color='r', label='Messwerte der Phasenverschiebung')
ax.scatter(phase(-1 * f, noms(RC)*1e-6), Uc/Uc[0], marker='x', color='navy', linewidth=0.8, label='Messwerte des Amplitudenverhältnis')
plt.polar(phase(-1 * f, noms(RC)*1e-6), g(f, noms(RC)*1e-6), label='Ausgleichsfunktion für die Zeitkonstante aus 4c',
        linewidth=0.5, color='green')

ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
plt.legend(loc="lower center")

plt.savefig('build/plot4.pdf')
plt.clf() 