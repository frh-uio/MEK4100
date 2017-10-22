import numpy as np
from math import sqrt, exp
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

axis_font = {'fontname':'Arial', 'size':'22'}
N = 100
x = np.linspace(0,1,N)
eps = 0.01
y_unified = np.zeros(N)

for i in range(len(x)):
	y_unified[i] = exp((-1+x[i])/eps) + exp(-x[i]/sqrt(eps))

plt.plot (x, y_unified)
plt.xlim([0, 1.1])
plt.xlabel('x', **axis_font)
plt.ylabel('$y_{unified}$', **axis_font)
plt.show()