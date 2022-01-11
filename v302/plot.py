import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit                        # Funktionsfit:     popt, pcov = curve_fit(func, xdata, ydata) 
from uncertainties import ufloat                            # Fehler:           fehlerwert =  ulfaot(x, err)
from uncertainties.unumpy import uarray                     # Array von Fehler: fehlerarray =  uarray(array, errarray)
from uncertainties.unumpy import (nominal_values as noms,   # Wert:             noms(fehlerwert) = x
                                  std_devs as stds)         # Abweichung:       stds(fehlerarray) = errarray
from uncertainties import unumpy as unp 
import scipy.constants as const

md = pd.read_csv('tables/e.csv')
md = md.iloc[:,[0,1]]
np.savetxt('tables/md.txt', md.values, header='nu/Hz U/mV', fmt='%.1f')

nu, Ubr = np.genfromtxt('tables/md.txt', unpack=True, skip_header=1)
Us = 4e3
nu0 = 50000/(33*2*const.pi)
Omega = nu/nu0
U = Ubr/Us

plt.plot(Omega, U, 'xr', linewidth = 1, label = 'Messdaten', alpha = 0.5)

def f(o):
    return np.sqrt( ((o**2 -1)**2) / (9 * ((1-o**2)**2) + 9*o**2)  )

xx = np.linspace(0, 150, 10000)
plt.plot(xx, f(xx), '-b', linewidth = 1, label = 'Theoriekurve')

plt.xlabel(r'$\Omega = \frac{\nu}{\nu_0}$')
plt.ylabel(r'$\frac{U_\mathrm{Br}}{U_\mathrm{S}}$')
plt.xscale('log')
plt.legend(loc="best")
plt.grid(True)

plt.xlim(0.1, 150)
plt.ylim(0)

plt.savefig('build/plot.pdf', bbox_inches = "tight")
plt.clf() 