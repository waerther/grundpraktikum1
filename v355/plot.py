import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp

frequenz = pd.read_csv('md_frequenz.csv')
frequenz = frequenz.iloc[:,:]
np.savetxt('frequenz.txt', frequenz.values, header='nu^+ nu^-', fmt='%.3f')
ck, nu_p, n_m = np.genfromtxt('frequenz.txt', unpack=True, skip_header=1)

def nu_minus(l, c, ck):
    return (1/(2*np.pi)) * ( l * ( (1/c) + (2/ck) )**(-1) )**(-1/2)

L = 0.023954
C = 0.7932e-9

x = np.linspace(0.997, 13, 120)
y = nu_minus(L, C, x*10**-9)

plt.plot(x, y*10**-3, '-r', label = 'Theoriewerte')
plt.plot(ck, n_m, 'xb', label = 'Messwerte')
plt.xlabel(r'$C_{K} \,/\, \mathrm{nF}$')
plt.ylabel(r'$\nu^- \,/\, \mathrm{kHz}$')
plt.legend(loc="best")
plt.xlim(0, 12.5)
plt.ylim(35, 58)
plt.grid(True)

plt.savefig('build/plot1.pdf', bbox_inches = "tight")
plt.clf() 