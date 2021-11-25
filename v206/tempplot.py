import matplotlib.pyplot as plt
import numpy as np

data_x = np.linspace(0, 500, 2000)
data_y = np.linspace(240, 10, 330)
np.savetxt('tempdaten.txt', np.column_stack([data_x, data_y]), header='t T_1 T_2')

plt.plot(x, x**2, label=r'$x^2$')
plt.plot(x, x**5, 'x', label=r'$x^5$')

x, y=  

# plt.subplot(1, 2, 2)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
# plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
# plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
