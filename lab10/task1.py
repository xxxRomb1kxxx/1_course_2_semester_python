import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 400)
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
plt.figure(figsize=(10, 6))
plt.title('Legendre polynomials')
for n in range(1, 8):
    Pn = legendre(n)
    plt.plot(x, Pn(x), label=f'n = {n}', color=colors[n-1])

plt.legend(loc='best')
plt.grid(True)
plt.show()
