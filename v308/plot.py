import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Lange Spule
x, y = np.genfromtxt('lange_spule.txt', unpack=True, skip_header=1)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Lange Spule')
ax.set_xlabel('x / m')
ax.set_ylabel('B / mT')
ax.grid()
ax.plot(x,y, 'x', label='Messwerte')
ax.legend()

plt.savefig('build/LangeSpule1.pdf')
plt.clf() 

# Helmholtz 1
x, y = np.genfromtxt('helmholtzspule_12cm.txt', unpack=True, skip_header=1)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Helmholtzspulenpaar mit d = 12cm')
ax.set_xlabel('x / m')
ax.set_ylabel('B / mT')
ax.grid()
ax.plot(x,y, 'x', label='Messwerte')
ax.legend(loc="lower left")

plt.savefig('build/Helmholtz1.pdf')
plt.clf() 

# Helmholtz 2
x, y = np.genfromtxt('helmholtzspule_14cm.txt', unpack=True, skip_header=1)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Helmholtzspulenpaar mit d = 14cm')
ax.set_xlabel('x / m')
ax.set_ylabel('B / mT')
ax.grid()
ax.plot(x,y, 'x', label='Messwerte')
ax.legend()

plt.savefig('build/Helmholtz2.pdf')
plt.clf() 

# Helmholtz 3
x, y = np.genfromtxt('helmholtzspule_16cm.txt', unpack=True, skip_header=1)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Helmholtzspulenpaar mit d = 16cm')
ax.set_xlabel('x / m')
ax.set_ylabel('B / mT')
ax.grid()
ax.plot(x,y, 'x', label='Messwerte')
ax.legend()

plt.savefig('build/Helmholtz3.pdf')
plt.clf() 

#  Toroidspule
x = [9,  8,  7,  6,  5,  4,  3,  2,  1,  0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
y = [653.300,  638.700,  617.800,  596.000,  565.700,  529.600,  484.400,  420.700,  300.000,  -86.000, -118.000, -307.800, -434.800, -525.400, -579.900, -588.300, -625.000, -657.200, -684.900, -714.100, -696.900, -679.200, -661.400, -637.900, -610.000, -576.000, -535.200, -471.400, -345.300, -134.300,   75.500,  258.700,  388.600,  480.800,  543.100,  586.900,  626.700,  659.000,  686.400,  711.800]
x1 =[0, 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
y2 =[0.000, 64.900,  230.700,  351.500,  435.200,  496.800,  542.900,  582.100,  613.800,  641.500, 666.600]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Hysteresekurve')
ax.set_xlabel('I / A')
ax.set_ylabel('B / mT')
ax.grid()
ax.plot(x,y, 'x', label='Messwerte')
ax.plot(x1,y2,'ro', label='Neukurve')
ax.legend()

plt.savefig('build/Hysteresekurve.pdf')
plt.clf() 